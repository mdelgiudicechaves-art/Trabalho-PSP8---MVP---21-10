# Databricks notebook source
# MAGIC %md
# MAGIC # 01 · Bronze — ingestão do CSV bruto
# MAGIC **Objetivo:** ler `marketing_campaign.csv` (separado por TAB) do Volume do Unity Catalog e gravar em Delta **sem nenhuma alteração de conteúdo**.
# MAGIC Todas as colunas entram como texto (sem inferência de tipos), mais metadados de ingestão (`_ingestao_ts`, `_arquivo_origem`, `_lote_id`).
# MAGIC Tipagem e limpeza ficam para a camada Silver.

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

# 1. Garante schema e volume (idempotente)
import os, uuid
from pyspark.sql import functions as F

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")
caminho = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/{CSV_NAME}"
print("Arquivo esperado:", caminho)

# COMMAND ----------

# 2. Verifica se o CSV foi enviado ao Volume
if not os.path.exists(caminho):
    raise FileNotFoundError(
        f"CSV não encontrado em {caminho}. Envie o arquivo pela interface: "
        "Catalog > {CATALOG} > {SCHEMA} > {VOLUME} > Upload to this volume.".format(
            CATALOG=CATALOG, SCHEMA=SCHEMA, VOLUME=VOLUME))
print("Tamanho (bytes):", os.path.getsize(caminho))

# COMMAND ----------

# 3. Leitura bruta (tudo string) + metadados de ingestão
df = (spark.read.option("header", True).option("sep", "\t").option("inferSchema", False).csv(caminho))
df = (df.withColumn("_ingestao_ts", F.current_timestamp())
        .withColumn("_arquivo_origem", F.lit(caminho))
        .withColumn("_lote_id", F.lit(str(uuid.uuid4()))))

n = df.count()
print(f"Linhas: {n} | Colunas (com metadados): {len(df.columns)}")
if n == 0:
    raise ValueError("Bronze vazio: verifique o separador (TAB) e o arquivo.")

# COMMAND ----------

# 4. Grava Delta (overwrite para o job ser reexecutável)
(df.write.format("delta").mode("overwrite").option("overwriteSchema", "true")
   .saveAsTable(T("bronze_marketing_campaign")))
print("Tabela criada:", T("bronze_marketing_campaign"))
display(spark.sql(f"SELECT * FROM {T('bronze_marketing_campaign')} LIMIT 5"))

# COMMAND ----------

# 5. Evidência: histórico Delta e contagem
display(spark.sql(f"DESCRIBE HISTORY {T('bronze_marketing_campaign')}"))
display(spark.sql(f"SELECT COUNT(*) AS linhas FROM {T('bronze_marketing_campaign')}"))
