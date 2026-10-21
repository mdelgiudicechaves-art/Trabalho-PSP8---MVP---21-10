# Evidências a capturar

Salve em `evidencias/` com o nome sugerido e referencie no ponto do README que a sustenta (imagens legíveis).

| id | o que capturar | onde | nome sugerido do arquivo | onde referenciar |
|---|---|---|---|---|
| E1 | Volume com o CSV enviado (Catalog > Volumes) | Databricks: Catalog | e01_volume_csv.png | README §2 Dados |
| E2 | Tabela Delta Bronze: amostra + DESCRIBE HISTORY | Notebook 01 (saídas das células 4 e 5) | e02_bronze.png | README §3 (Bronze) |
| E3 | Silver: log de regras (silver_regras_negocio) e contagens | Notebook 02 (célula 2) | e03_silver_regras.png | README §3 (Qualidade/tratamento) |
| E4 | Catalog Explorer mostrando as tabelas bronze/silver/gold no schema | Databricks: Catalog > schema | e04_catalogo_tabelas.png | README §3 (tabelas Delta persistidas) |
| E5 | Esquema estrela: tabelas dim_* e fato_* com contagem de linhas | Notebook 03 (célula 2) | e05_estrela.png | README §3 (Modelo) |
| E6 | Escolha de k: cotovelo + silhouette + estabilidade (ARI) | Notebook 04 (P1a) | p1_cotovelo_silhouette.png | README §4 P1 |
| E7 | Perfil dos segmentos (tabela + mapa de calor) | Notebook 04 (P1b) | p1_perfil_segmentos.png | README §4 P1 |
| E8 | Receita por segmento e curva de Pareto | Notebook 04 (P2) | p2_receita_pareto.png | README §4 P2 |
| E9 | Mix de categorias, canais, visitas web e desconto | Notebook 04 (P3) | p3_mix_canal.png | README §4 P3 |
| E10 | Taxas de campanha e ROI estimado (premissa Z_*) | Notebook 04 (P4) | p4_campanhas_roi.png | README §4 P4 |
| E11 | Lista de clientes em risco (top 20) e contagem por segmento | Notebook 04 (P5) | p5_clientes_risco.png | README §4 P5 |
| E12 | Consulta SQL de uma visão (ex.: vw_perfil_segmento) | Databricks: SQL Editor / notebook 03 | e12_sql_vw_perfil.png | README §3 (visões) |
| E13 | Job/Workflow com 4 tarefas encadeadas e execução bem-sucedida | Databricks: Jobs & Pipelines > Runs | e13_job_execucao.png | README §3 (orquestração ETL) |
| E14 | Qualidade: outliers e categorias estranhas (já gerado no Colab) | Colab seção 5 | qualidade_outliers_categorias.png | README §3 (Qualidade) |
| E15 | Ensaio local da escolha de k (já gerado no Colab) | Colab seção 7 | ensaio_local_escolha_k.png | README §3 (Clusterização) |
| E16 | Repositório público aberto em janela anônima | GitHub | e16_repo_publico.png | Postagem no fórum |