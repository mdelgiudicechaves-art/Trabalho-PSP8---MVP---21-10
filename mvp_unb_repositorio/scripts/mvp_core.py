# ============================================================
# NÚCLEO DE LÓGICA DO MVP (usado no Colab e nos notebooks Databricks)
# Funções puras em pandas/sklearn: Silver (limpeza + features),
# clusterização (K-Means) e construção das tabelas do esquema estrela.
# Volume de dados pequeno (2.240 linhas): pandas é suficiente e testável.
# ============================================================
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, adjusted_rand_score

# ---------- Mapeamentos e nomes -------------------------------------------
RENOMEAR = {
    "ID": "cliente_id", "Year_Birth": "ano_nascimento", "Education": "educacao_original",
    "Marital_Status": "estado_civil_original", "Income": "renda",
    "Kidhome": "filhos_criancas", "Teenhome": "filhos_adolescentes",
    "Dt_Customer": "data_cadastro", "Recency": "recencia_dias",
    "MntWines": "gasto_vinhos", "MntFruits": "gasto_frutas", "MntMeatProducts": "gasto_carnes",
    "MntFishProducts": "gasto_peixes", "MntSweetProducts": "gasto_doces", "MntGoldProds": "gasto_ouro",
    "NumDealsPurchases": "compras_desconto", "NumWebPurchases": "compras_web",
    "NumCatalogPurchases": "compras_catalogo", "NumStorePurchases": "compras_loja",
    "NumWebVisitsMonth": "visitas_web_mes",
    "AcceptedCmp1": "campanha_1", "AcceptedCmp2": "campanha_2", "AcceptedCmp3": "campanha_3",
    "AcceptedCmp4": "campanha_4", "AcceptedCmp5": "campanha_5", "Response": "campanha_ultima",
    "Complain": "reclamacao_2anos",
}
CATEGORIAS = ["vinhos", "carnes", "peixes", "frutas", "doces", "ouro"]
COLS_GASTO = [f"gasto_{c}" for c in CATEGORIAS]
COLS_CAMPANHA = ["campanha_1", "campanha_2", "campanha_3", "campanha_4", "campanha_5", "campanha_ultima"]
MAP_EDUCACAO = {  # original -> (padronizada, nível ordinal)
    "Basic": ("Básico", 1), "Graduation": ("Graduação", 2),
    "2n Cycle": ("Mestrado", 3),  # premissa: 2n Cycle = 2º ciclo (Bologna) ~ mestrado
    "Master": ("Mestrado", 3), "PhD": ("Doutorado", 4),
}
MAP_ESTADO_CIVIL = {  # original -> (padronizado, grupo)
    "Married": ("Casado(a)", "Com parceiro(a)"), "Together": ("União estável", "Com parceiro(a)"),
    "Single": ("Solteiro(a)", "Sem parceiro(a)"), "Alone": ("Solteiro(a)", "Sem parceiro(a)"),
    "Divorced": ("Divorciado(a)", "Sem parceiro(a)"), "Widow": ("Viúvo(a)", "Sem parceiro(a)"),
    "Absurd": ("Não informado", "Não informado"), "YOLO": ("Não informado", "Não informado"),
}
FEATURES_CLUSTER = ["recencia_dias", "compras_total", "gasto_total_log", "renda", "idade", "n_filhos"]


def _num(df, cols):
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="raise")
    return df


# ---------- SILVER ---------------------------------------------------------
def silver_transform(raw):
    """Recebe o Bronze (pandas) e devolve (silver, log).
    log = lista de dicts {regra, afetados, decisao} para documentar cada regra de negócio."""
    log = []
    df = raw[[c for c in raw.columns if not c.startswith("_")]].copy()  # remove metadados de ingestão
    textos = ["Education", "Marital_Status", "Dt_Customer"]
    df = _num(df, [c for c in df.columns if c not in textos])

    # R1. Colunas constantes não carregam informação -> descartadas (valores guardados como premissa de P4)
    constantes = {c: df[c].iloc[0] for c in df.columns if df[c].nunique(dropna=False) == 1}
    df = df.drop(columns=list(constantes))
    log.append({"regra": "R1 Colunas constantes", "afetados": len(constantes),
                "decisao": f"Descartadas {list(constantes)} (valores {list(constantes.values())}); "
                           "mantidos só como premissa de custo/receita em P4"})

    df = df.rename(columns=RENOMEAR)

    # R2. Datas: Dt_Customer vem como dd-mm-aaaa
    df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], format="%d-%m-%Y", errors="raise")
    data_ref = df["data_cadastro"].max()  # idade/tempo calculados na data de referência da base, não hoje
    log.append({"regra": "R2 Data de referência", "afetados": len(df),
                "decisao": f"data_ref = max(Dt_Customer) = {data_ref.date()}; idade e tempo de cliente calculados nela"})

    # R3. Renda: nulos + outlier extremo (> Q3 + 3*IQR) -> NaN -> imputação pela mediana do nível de educação
    q1, q3 = df["renda"].quantile([.25, .75])
    limite = q3 + 3 * (q3 - q1)
    m_out = df["renda"] > limite
    m_nulo = df["renda"].isna()
    df["flag_renda_outlier"] = m_out
    df["flag_renda_imputada"] = m_out | m_nulo
    base = df.loc[~(m_out | m_nulo)]
    med_educ = base.groupby("educacao_original")["renda"].median()
    df.loc[m_out, "renda"] = np.nan
    df["renda"] = df["renda"].fillna(df["educacao_original"].map(med_educ)).fillna(base["renda"].median())
    log.append({"regra": "R3 Renda nula", "afetados": int(m_nulo.sum()),
                "decisao": "Imputada pela mediana de renda do mesmo nível de educação (flag_renda_imputada)"})
    log.append({"regra": "R4 Renda outlier extremo", "afetados": int(m_out.sum()),
                "decisao": f"Valores > {limite:,.0f} (Q3+3·IQR) tratados como erro de digitação: viram nulo e são imputados"})

    # R5. Idade implausível
    df["idade"] = data_ref.year - df["ano_nascimento"]
    m_idade = (df["idade"] > 100) | (df["idade"] < 16)
    df["flag_idade_corrigida"] = m_idade
    df.loc[m_idade, "idade"] = np.nan
    df["idade"] = df["idade"].fillna(df["idade"].median()).astype(int)
    df["ano_nascimento"] = (data_ref.year - df["idade"]).astype(int)
    log.append({"regra": "R5 Idade implausível", "afetados": int(m_idade.sum()),
                "decisao": "Idade > 100 ou < 16 na data de referência vira nulo e é imputada pela mediana (flag_idade_corrigida)"})

    # R6. Padronização de categorias
    desconhecidas = set(df["educacao_original"]) - set(MAP_EDUCACAO)
    desconhecidas |= set(df["estado_civil_original"]) - set(MAP_ESTADO_CIVIL)
    if desconhecidas:
        raise ValueError(f"Categorias não mapeadas: {desconhecidas}. Atualize MAP_EDUCACAO / MAP_ESTADO_CIVIL.")
    df["educacao"] = df["educacao_original"].map(lambda x: MAP_EDUCACAO[x][0])
    df["educacao_nivel"] = df["educacao_original"].map(lambda x: MAP_EDUCACAO[x][1])
    df["estado_civil"] = df["estado_civil_original"].map(lambda x: MAP_ESTADO_CIVIL[x][0])
    df["estado_civil_grupo"] = df["estado_civil_original"].map(lambda x: MAP_ESTADO_CIVIL[x][1])
    n_est = int(df["estado_civil_original"].isin(["Alone", "Absurd", "YOLO"]).sum())
    log.append({"regra": "R6 Estado civil", "afetados": n_est,
                "decisao": "Alone -> Solteiro(a); Absurd e YOLO -> 'Não informado' (mantidos, sem inferir valor)"})
    log.append({"regra": "R7 Educação '2n Cycle'", "afetados": int((df["educacao_original"] == "2n Cycle").sum()),
                "decisao": "Premissa: 2º ciclo (Bologna) equivale a Mestrado; coluna original preservada"})

    # R8. Features derivadas
    df["gasto_total"] = df[COLS_GASTO].sum(axis=1)
    df["compras_total"] = df[["compras_web", "compras_catalogo", "compras_loja"]].sum(axis=1)  # canais; desconto é subconjunto
    df["n_filhos"] = df["filhos_criancas"] + df["filhos_adolescentes"]
    df["tempo_cliente_dias"] = (data_ref - df["data_cadastro"]).dt.days
    df["flag_sem_compras"] = df["compras_total"] == 0
    comp = df["compras_total"].replace(0, np.nan)
    df["ticket_medio"] = (df["gasto_total"] / comp).fillna(0.0)
    for canal in ["web", "catalogo", "loja"]:
        df[f"share_{canal}"] = (df[f"compras_{canal}"] / comp).fillna(0.0)
    df["pct_compras_desconto"] = (df["compras_desconto"] / comp).clip(upper=1).fillna(0.0)
    for c in CATEGORIAS:
        df[f"pct_gasto_{c}"] = df[f"gasto_{c}"] / df["gasto_total"].replace(0, np.nan)
        df[f"pct_gasto_{c}"] = df[f"pct_gasto_{c}"].fillna(0.0)
    df["n_campanhas_aceitas"] = df[COLS_CAMPANHA[:5]].sum(axis=1)  # campanhas 1 a 5
    log.append({"regra": "R8 Features", "afetados": len(df),
                "decisao": "gasto_total, compras_total (web+catálogo+loja; desconto é subconjunto), n_filhos, "
                           "tempo_cliente_dias, ticket_medio, share por canal, pct por categoria, n_campanhas_aceitas"})
    n_desc = int((df["compras_desconto"] > df["compras_total"]).sum())
    log.append({"regra": "R9 Consistência: compras com desconto > compras totais", "afetados": n_desc,
                "decisao": "Mantidos; pct_compras_desconto limitado a 1 (inconsistência registrada, não corrigida)"})
    log.append({"regra": "R10 Clientes sem compras", "afetados": int(df["flag_sem_compras"].sum()),
                "decisao": "Mantidos (têm gasto > 0); ticket médio e shares ficam 0 (flag_sem_compras)"})

    ordem = ["cliente_id", "ano_nascimento", "idade", "data_cadastro", "educacao_original", "educacao",
             "educacao_nivel", "estado_civil_original", "estado_civil", "estado_civil_grupo", "renda",
             "filhos_criancas", "filhos_adolescentes", "n_filhos", "recencia_dias", "tempo_cliente_dias"]
    resto = [c for c in df.columns if c not in ordem]
    df = df[ordem + resto].reset_index(drop=True)
    for c in ["flag_renda_outlier", "flag_renda_imputada", "flag_idade_corrigida", "flag_sem_compras"]:
        df[c] = df[c].astype(bool)
    return df, pd.DataFrame(log), {k: float(v) for k, v in constantes.items()}


# ---------- CLUSTERIZAÇÃO ---------------------------------------------------
def matriz_cluster(silver):
    X = silver.copy()
    X["gasto_total_log"] = np.log1p(X["gasto_total"])  # reduz assimetria do gasto
    Z = StandardScaler().fit_transform(X[FEATURES_CLUSTER])
    return Z


def clusterizar(silver, k_plot_min=2, k_max=8, k_min_escolha=3, seed=42, seeds_estab=(1, 7, 21, 42, 99)):
    """K-Means. Escolhe k pelo maior silhouette em [k_min_escolha, k_max]; mede estabilidade (ARI entre sementes)."""
    Z = matriz_cluster(silver)
    linhas = []
    for k in range(k_plot_min, k_max + 1):
        km = KMeans(n_clusters=k, n_init=20, random_state=seed).fit(Z)
        linhas.append({"k": k, "inercia": km.inertia_, "silhouette": silhouette_score(Z, km.labels_)})
    metricas = pd.DataFrame(linhas)
    elegiveis = metricas[metricas["k"] >= k_min_escolha]
    k = int(elegiveis.loc[elegiveis["silhouette"].idxmax(), "k"])
    base = KMeans(n_clusters=k, n_init=20, random_state=seed).fit(Z).labels_
    aris = []
    for s in seeds_estab:
        outro = KMeans(n_clusters=k, n_init=20, random_state=s).fit(Z).labels_
        aris.append(adjusted_rand_score(base, outro))
    estab = {"k": k, "ari_medio": float(np.mean(aris)), "ari_min": float(np.min(aris)),
             "sementes": list(seeds_estab), "silhouette_k": float(metricas.loc[metricas.k == k, "silhouette"].iloc[0])}
    # ordena segmentos por gasto médio decrescente: S1 = maior gasto
    tmp = pd.DataFrame({"lab": base, "gasto": silver["gasto_total"].values})
    ordem = tmp.groupby("lab")["gasto"].mean().sort_values(ascending=False).index.tolist()
    novo = {lab: i + 1 for i, lab in enumerate(ordem)}
    seg_id = pd.Series(base).map(novo).astype(int).values
    return seg_id, metricas, estab


def rotulo_segmento(i, k):
    if i == 1:
        return f"S{i} - maior gasto"
    if i == k:
        return f"S{i} - menor gasto"
    return f"S{i} - gasto intermediário"


# ---------- GOLD: esquema estrela -------------------------------------------
def construir_gold(silver, seg_id):
    s = silver.copy()
    s["segmento_id"] = seg_id
    k = int(s["segmento_id"].max())

    dim_educacao = (s[["educacao_original", "educacao", "educacao_nivel"]].drop_duplicates()
                    .sort_values(["educacao_nivel", "educacao_original"]).reset_index(drop=True))
    dim_educacao.insert(0, "educacao_id", range(1, len(dim_educacao) + 1))
    dim_estado = (s[["estado_civil", "estado_civil_grupo"]].drop_duplicates()
                  .sort_values("estado_civil").reset_index(drop=True))
    dim_estado.insert(0, "estado_civil_id", range(1, len(dim_estado) + 1))

    datas = pd.Series(pd.to_datetime(s["data_cadastro"].unique())).sort_values()
    dim_tempo = pd.DataFrame({"data": datas})
    dim_tempo.insert(0, "data_id", dim_tempo["data"].dt.strftime("%Y%m%d").astype(int))
    dim_tempo["ano"] = dim_tempo["data"].dt.year
    dim_tempo["trimestre"] = dim_tempo["data"].dt.quarter
    dim_tempo["mes"] = dim_tempo["data"].dt.month
    dim_tempo["dia_semana"] = dim_tempo["data"].dt.dayofweek + 1  # 1=segunda
    dim_tempo["ano_mes"] = dim_tempo["data"].dt.strftime("%Y-%m")

    dim_cliente = s[["cliente_id", "ano_nascimento", "idade", "renda", "n_filhos", "filhos_criancas",
                     "filhos_adolescentes", "flag_renda_outlier", "flag_renda_imputada",
                     "flag_idade_corrigida"]].copy()
    dim_cliente["faixa_etaria"] = pd.cut(dim_cliente["idade"], [0, 34, 44, 54, 64, 200],
                                         labels=["até 34", "35-44", "45-54", "55-64", "65+"]).astype(str)
    dim_cliente["faixa_renda"] = pd.qcut(dim_cliente["renda"], 4, labels=["Q1 (menor)", "Q2", "Q3", "Q4 (maior)"]).astype(str)
    dim_cliente["tem_filhos"] = dim_cliente["n_filhos"] > 0

    agg = s.groupby("segmento_id").agg(n_clientes=("cliente_id", "count"), gasto_medio=("gasto_total", "mean"),
                                       renda_media=("renda", "mean"), recencia_media=("recencia_dias", "mean")).reset_index()
    agg["rotulo"] = [rotulo_segmento(i, k) for i in agg["segmento_id"]]
    dim_segmento = agg[["segmento_id", "rotulo", "n_clientes", "gasto_medio", "renda_media", "recencia_media"]]

    fato = s.merge(dim_educacao[["educacao_id", "educacao_original"]], on="educacao_original") \
            .merge(dim_estado[["estado_civil_id", "estado_civil"]], on="estado_civil")
    fato["data_id"] = fato["data_cadastro"].dt.strftime("%Y%m%d").astype(int)
    cols_fato = (["cliente_id", "educacao_id", "estado_civil_id", "data_id", "segmento_id", "recencia_dias",
                  "tempo_cliente_dias", "gasto_total"] + COLS_GASTO +
                 [f"pct_gasto_{c}" for c in CATEGORIAS] +
                 ["compras_total", "compras_web", "compras_catalogo", "compras_loja", "compras_desconto",
                  "visitas_web_mes", "ticket_medio", "share_web", "share_catalogo", "share_loja",
                  "pct_compras_desconto"] + COLS_CAMPANHA + ["n_campanhas_aceitas", "reclamacao_2anos", "flag_sem_compras"])
    fato = fato[cols_fato].sort_values("cliente_id").reset_index(drop=True)
    assert len(fato) == len(s), "O join da fato duplicou ou perdeu clientes"
    return {"dim_cliente": dim_cliente, "dim_educacao": dim_educacao, "dim_estado_civil": dim_estado,
            "dim_tempo": dim_tempo, "dim_segmento": dim_segmento, "fato_cliente_vendas": fato}
