# Databricks notebook source
# MAGIC %md
# MAGIC # 04 · Análise — respostas a P1–P5
# MAGIC Cada seção traz: consulta (SQL/pandas) → gráfico → **discussão**. Todos os números vêm da execução; os trechos entre colchetes `[preencher ...]` devem ser completados **depois** de rodar, olhando as saídas.
# MAGIC Resultados fracos ou inconclusivos devem ser relatados como tal.

# COMMAND ----------

# Configuração (preenchida pelo Colab; pode editar aqui se rodar manualmente)
CATALOG = "workspace"        # Free Edition: catálogo padrão costuma ser "workspace"
SCHEMA  = "mvp_marketing"
VOLUME  = "raw"
CSV_NAME = "marketing_campaign.csv"
SEED = 42
K_MAX = 8
K_MIN_ESCOLHA = 3
PCT_RISCO_GASTO = 0.75   # cliente de alto gasto = acima deste percentil
PCT_RISCO_RECENCIA = 0.75  # recência alta (muitos dias sem comprar) = acima deste percentil
N_CONTATOS_POR_CLIENTE = 6      # premissa P4: cada cliente recebeu as 6 campanhas (1 a 5 + última)

def T(nome):
    """Nome totalmente qualificado de uma tabela/view."""
    return f"{CATALOG}.{SCHEMA}.{nome}"

# COMMAND ----------

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
def q(sql):
    return spark.sql(sql).toPandas()
def seg_cores(rotulos):
    paleta = ["#2a6f97", "#e07a1f", "#6a994e", "#b5446e", "#7a6fb5", "#8d8d8d", "#c9a227", "#2a9d8f"]
    return {r: paleta[i % len(paleta)] for i, r in enumerate(sorted(rotulos))}
perfil = q(f"SELECT * FROM {T('vw_perfil_segmento')} ORDER BY segmento_id")
CORES = seg_cores(perfil["rotulo"])

# COMMAND ----------

# MAGIC %md
# MAGIC ## P1 · Quantos segmentos naturais existem e qual o perfil de cada um?

# COMMAND ----------

# P1a. Escolha de k: cotovelo (inércia) e silhouette
m = q(f"SELECT * FROM {T('gold_clusterizacao_metricas')} ORDER BY k")
est = q(f"SELECT * FROM {T('gold_clusterizacao_estabilidade')}")
k_esc = int(est["k"].iloc[0])
fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
ax[0].plot(m["k"], m["inercia"], marker="o", color="#2a6f97"); ax[0].set_title("Método do cotovelo (inércia)")
ax[0].set_xlabel("k"); ax[0].axvline(k_esc, ls="--", color="#999")
ax[1].plot(m["k"], m["silhouette"], marker="o", color="#e07a1f"); ax[1].set_title("Silhouette médio")
ax[1].set_xlabel("k"); ax[1].axvline(k_esc, ls="--", color="#999")
plt.tight_layout(); plt.show()
display(m); display(est)

# COMMAND ----------

# P1b. Perfil dos segmentos (tabela + mapa de calor padronizado por coluna)
display(perfil)
cols = ["renda_media", "idade_media", "filhos_medio", "gasto_medio", "compras_media", "recencia_media", "ticket_medio", "visitas_web_media"]
z = (perfil[cols] - perfil[cols].mean()) / perfil[cols].std(ddof=0).replace(0, 1)
fig, ax = plt.subplots(figsize=(9, 0.9 + 0.7 * len(perfil)))
im = ax.imshow(z.values, cmap="RdBu_r", vmin=-1.6, vmax=1.6, aspect="auto")
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=30, ha="right")
ax.set_yticks(range(len(perfil))); ax.set_yticklabels(perfil["rotulo"])
for i in range(len(perfil)):
    for j, c in enumerate(cols):
        ax.text(j, i, f"{perfil[c].iloc[i]:,.1f}", ha="center", va="center", fontsize=8)
ax.set_title("Perfil por segmento (cor = desvio em relação à média dos segmentos)")
plt.colorbar(im, ax=ax, shrink=0.8); plt.tight_layout(); plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Discussão P1
# MAGIC - **Número de segmentos:** o silhouette indicou k = **[preencher após executar]** com valor **[preencher]**. Valores de silhouette abaixo de ~0,35 indicam grupos **pouco separados**: se for o caso, relate que os segmentos são mais um *contínuo de valor* (renda/gasto) do que grupos naturais bem delimitados.
# MAGIC - **Por que não k=2:** [preencher: k=2 costuma separar apenas "alto" × "baixo" valor, o que é pouco acionável; a escolha de k ≥ `K_MIN_ESCOLHA` é uma decisão de negócio, declarada].
# MAGIC - **Estabilidade:** ARI médio entre sementes = **[preencher]** (próximo de 1 indica partição reprodutível).
# MAGIC - **Perfis:** [preencher: descreva cada segmento em renda, filhos, gasto e frequência olhando a tabela/mapa de calor].

# COMMAND ----------

# MAGIC %md
# MAGIC ## P2 · Contribuição de cada segmento para a receita e concentração (Pareto 80%)

# COMMAND ----------

rec = q(f"SELECT * FROM {T('vw_receita_segmento')} ORDER BY segmento_id")
display(rec)
x = np.arange(len(rec)); w = 0.38
fig, ax = plt.subplots(figsize=(8, 3.6))
ax.bar(x - w/2, rec["pct_clientes"] * 100, w, label="% dos clientes", color="#bdbdbd")
ax.bar(x + w/2, rec["pct_receita"] * 100, w, label="% do gasto (receita)", color="#2a6f97")
ax.set_xticks(x); ax.set_xticklabels(rec["rotulo"], rotation=15); ax.set_ylabel("%"); ax.legend()
ax.set_title("Participação no gasto total × participação nos clientes")
plt.tight_layout(); plt.show()

# Pareto: fração de clientes que concentra 80% do gasto
g = q(f"SELECT cliente_id, gasto_total FROM {T('fato_cliente_vendas')}").sort_values("gasto_total", ascending=False).reset_index(drop=True)
g["pct_acum_gasto"] = g["gasto_total"].cumsum() / g["gasto_total"].sum()
g["pct_acum_clientes"] = (g.index + 1) / len(g)
n80 = int((g["pct_acum_gasto"] < 0.80).sum() + 1)
frac80 = n80 / len(g)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(g["pct_acum_clientes"] * 100, g["pct_acum_gasto"] * 100, color="#2a6f97")
ax.axhline(80, ls="--", color="#999"); ax.axvline(frac80 * 100, ls="--", color="#999")
ax.set_xlabel("% acumulado de clientes (do maior para o menor gasto)"); ax.set_ylabel("% acumulado do gasto")
ax.set_title(f"Pareto: {frac80:.1%} dos clientes ({n80}) concentram 80% do gasto")
plt.tight_layout(); plt.show()
print(f"{n80} clientes ({frac80:.1%}) concentram 80% do gasto total.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Discussão P2
# MAGIC - **Receita por segmento:** o segmento **[preencher]** responde por **[preencher]%** do gasto com **[preencher]%** dos clientes; gasto médio por cliente: [preencher].
# MAGIC - **Pareto:** **[preencher]%** dos clientes concentram 80% do gasto. Se for bem acima de 20%, a concentração é **menor que a regra 80/20 clássica** — diga isso explicitamente.
# MAGIC - **Implicação comercial:** [preencher: quanto vale priorizar o segmento de maior gasto].

# COMMAND ----------

# MAGIC %md
# MAGIC ## P3 · Mix de categorias, canais, visitas web e compras com desconto

# COMMAND ----------

mix = q(f"SELECT * FROM {T('vw_mix_canal_segmento')} ORDER BY segmento_id")
display(mix)
cats = ["mix_vinhos", "mix_carnes", "mix_peixes", "mix_frutas", "mix_doces", "mix_ouro"]
canais = ["canal_loja", "canal_web", "canal_catalogo"]
fig, ax = plt.subplots(1, 2, figsize=(11, 3.8))
for a, cols, titulo in [(ax[0], cats, "Mix de categorias (% do gasto)"), (ax[1], canais, "Canal (% das compras)")]:
    base = np.zeros(len(mix))
    for c in cols:
        a.bar(mix["rotulo"], mix[c] * 100, bottom=base, label=c.split("_")[1]); base += mix[c].values * 100
    a.set_title(titulo); a.set_ylabel("%"); a.tick_params(axis="x", rotation=15); a.legend(fontsize=8, ncol=2)
plt.tight_layout(); plt.show()

fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
ax[0].bar(mix["rotulo"], mix["visitas_web_media"], color="#7a6fb5"); ax[0].set_title("Visitas web/mês (média)")
ax[1].bar(mix["rotulo"], mix["pct_compras_desconto"] * 100, color="#b5446e"); ax[1].set_title("% das compras com desconto")
for a in ax: a.tick_params(axis="x", rotation=15)
plt.tight_layout(); plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Discussão P3
# MAGIC - **Mix:** vinhos representam [preencher]% do gasto no total; os segmentos diferem principalmente em [preencher: categorias com maior diferença].
# MAGIC - **Canal:** a loja física concentra [preencher]% das compras; [preencher: segmento que mais usa web e catálogo].
# MAGIC - **Visitas web e desconto:** [preencher: relação entre muitas visitas web, compras com desconto e baixo gasto — **descreva como associação**, não como causalidade; a base não permite inferir causa].

# COMMAND ----------

# MAGIC %md
# MAGIC ## P4 · Aceitação de campanhas e retorno estimado por segmento
# MAGIC **Premissa declarada:** a base **não documenta** `Z_CostContact` e `Z_Revenue`. Assumimos custo por contato = `Z_CostContact` (3) e receita por aceite = `Z_Revenue` (11), e que **cada cliente foi contatado nas 6 campanhas** (1 a 5 e a última). Os resultados abaixo dependem inteiramente dessa premissa.

# COMMAND ----------

camp = q(f"SELECT * FROM {T('vw_campanhas_segmento')} ORDER BY segmento_id")
camp["retorno_estimado"] = camp["receita_estimada"] - camp["custo_estimado"]
camp["roi_estimado"] = camp["retorno_estimado"] / camp["custo_estimado"]
camp["retorno_por_contato"] = camp["retorno_estimado"] / camp["contatos"]
display(camp)
taxas = ["taxa_c1", "taxa_c2", "taxa_c3", "taxa_c4", "taxa_c5", "taxa_ultima"]
fig, ax = plt.subplots(figsize=(8, 0.9 + 0.7 * len(camp)))
im = ax.imshow(camp[taxas].values * 100, cmap="Blues", aspect="auto")
ax.set_xticks(range(6)); ax.set_xticklabels(["Cmp1", "Cmp2", "Cmp3", "Cmp4", "Cmp5", "Última"])
ax.set_yticks(range(len(camp))); ax.set_yticklabels(camp["rotulo"])
for i in range(len(camp)):
    for j, c in enumerate(taxas):
        ax.text(j, i, f"{camp[c].iloc[i]*100:.1f}%", ha="center", va="center", fontsize=8)
ax.set_title("Taxa de aceitação por campanha e segmento"); plt.tight_layout(); plt.show()
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.bar(camp["rotulo"], camp["roi_estimado"], color=[CORES[r] for r in camp["rotulo"]])
ax.axhline(0, color="#444", lw=0.8); ax.set_ylabel("ROI estimado"); ax.set_title("ROI estimado por segmento (sob a premissa de Z_*)")
ax.tick_params(axis="x", rotation=15); plt.tight_layout(); plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Discussão P4
# MAGIC - **Aceitação:** a taxa varia de [preencher] a [preencher] entre segmentos; [preencher: campanha com menor/maior aceitação no geral — a base mostra taxas baixas (< ~15%), o que limita a precisão das comparações em segmentos pequenos].
# MAGIC - **Retorno estimado:** o segmento com melhor retorno por contato é **[preencher]** (ROI [preencher]). **Lembrete:** é estimativa sob premissa; se Z_* tiver outro significado, a conclusão pode mudar.
# MAGIC - **Limite:** `Response` refere-se a **uma única campanha**; não há dados de custo real nem de margem.

# COMMAND ----------

# MAGIC %md
# MAGIC ## P5 · Clientes de alto gasto e recência alta (risco de inatividade)
# MAGIC Definição: gasto total ≥ percentil `PCT_RISCO_GASTO` **e** dias desde a última compra ≥ percentil `PCT_RISCO_RECENCIA`. (Na base, `Recency` = dias desde a última compra; valor alto = cliente parado há mais tempo.)

# COMMAND ----------

risco = q(f"SELECT * FROM {T('vw_clientes_risco')} ORDER BY gasto_total DESC")
print(f"{len(risco)} clientes em risco ({len(risco)/spark.table(T('fato_cliente_vendas')).count():.1%} da base) "
      f"| gasto somado: {risco['gasto_total'].sum():,.0f}")
display(risco.head(20))
por_seg = risco.groupby("rotulo").agg(clientes=("cliente_id", "count"), gasto=("gasto_total", "sum"), recencia_media=("recencia_dias", "mean")).reset_index()
display(por_seg)
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.bar(por_seg["rotulo"], por_seg["clientes"], color=[CORES[r] for r in por_seg["rotulo"]])
ax.set_title("Clientes em risco por segmento"); ax.tick_params(axis="x", rotation=15)
plt.tight_layout(); plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Discussão P5
# MAGIC - **Tamanho do risco:** [preencher] clientes (gasto somado [preencher]) estão em alto gasto + recência alta, concentrados em [preencher: segmento].
# MAGIC - **Ação sugerida:** contato proativo e personalizado pelo canal preferido do cliente (loja/web/catálogo), com oferta ligada à categoria dominante dele (ver P3); medir reativação em 30–60 dias.
# MAGIC - **Cautela:** recência alta pode refletir ciclo de compra natural (ex.: vinho premium), não abandono; validar com histórico de compras, que a base não traz.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Discussão geral e playbook comercial
# MAGIC **Hipótese testada:** existem segmentos com valor, comportamento e resposta a campanhas diferentes? **[preencher: confirmada / parcialmente confirmada / não confirmada, com base em P1–P4 e na separação dos clusters]**.
# MAGIC
# MAGIC ### Playbook (uma ação por segmento) — complete após ver os perfis
# MAGIC | Segmento | Perfil resumido | Oferta | Canal | Prioridade |
# MAGIC |---|---|---|---|---|
# MAGIC | S1 - maior gasto | [preencher] | [ex.: curadoria premium/fidelização, conforme categoria dominante] | [preencher conforme canal dominante] | [alta, se ROI e receita altos] |
# MAGIC | S2 e demais intermediários | [preencher] | [ex.: cross-sell para a 2ª categoria mais comprada] | [preencher] | [preencher] |
# MAGIC | S_último - menor gasto | [preencher] | [ex.: ofertas de entrada/desconto, custo baixo] | [ex.: web/e-mail, de menor custo] | [baixa/automatizada] |
# MAGIC | Clientes em risco (P5) | alto gasto + parados | reativação personalizada | canal preferido | alta |
# MAGIC
# MAGIC ### Limitações
# MAGIC Dados de ~2012–2014 (podem estar defasados); sem custo/margem por produto; significado de Z_* é premissa; `Response` é de uma campanha; amostra com possível viés de seleção; segmentos pouco separados limitam a generalização.
