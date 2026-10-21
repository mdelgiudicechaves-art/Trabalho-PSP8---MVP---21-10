# Catálogo de Dados

Dataset: Kaggle `imakash3011/customer-personality-analysis` · Licença: CC0: Public Domain · Extração: 2026-10-21


## bronze_marketing_campaign

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| ID | numérico (chave) | Identificador sequencial do cliente (não é identificador direto) | inteiro, 0 a 11191, únicos=2240 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Year_Birth | numérico | Ano de nascimento | 1893 a 1996 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Education | categórico | Nível de escolaridade | 2n Cycle; Basic; Graduation; Master; PhD | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Marital_Status | categórico | Estado civil | Absurd; Alone; Divorced; Married; Single; Together; Widow; YOLO | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Income | numérico | Renda anual do domicílio | 1730 a 666666 | Admite nulos (24); ausência = valor não informado na origem | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original; 24 nulos |
| Kidhome | numérico | Nº de crianças no domicílio | 0 a 2 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Teenhome | numérico | Nº de adolescentes no domicílio | 0 a 2 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Dt_Customer | texto | Data de cadastro do cliente (dd-mm-aaaa) | 663 valores distintos | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original (texto) |
| Recency | numérico | Dias desde a última compra | 0 a 99 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntWines | numérico | Gasto com vinhos nos últimos 2 anos | 0 a 1493 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntFruits | numérico | Gasto com frutas nos últimos 2 anos | 0 a 199 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntMeatProducts | numérico | Gasto com carnes nos últimos 2 anos | 0 a 1725 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntFishProducts | numérico | Gasto com peixes nos últimos 2 anos | 0 a 259 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntSweetProducts | numérico | Gasto com doces nos últimos 2 anos | 0 a 263 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| MntGoldProds | numérico | Gasto com produtos premium (ouro) nos últimos 2 anos | 0 a 362 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| NumDealsPurchases | numérico | Compras feitas com desconto | 0 a 15 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| NumWebPurchases | numérico | Compras pelo site | 0 a 27 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| NumCatalogPurchases | numérico | Compras por catálogo | 0 a 28 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| NumStorePurchases | numérico | Compras em loja física | 0 a 13 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| NumWebVisitsMonth | numérico | Visitas ao site no último mês | 0 a 20 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| AcceptedCmp3 | numérico | Aceitou a oferta da campanha 3 (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| AcceptedCmp4 | numérico | Aceitou a oferta da campanha 4 (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| AcceptedCmp5 | numérico | Aceitou a oferta da campanha 5 (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| AcceptedCmp1 | numérico | Aceitou a oferta da campanha 1 (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| AcceptedCmp2 | numérico | Aceitou a oferta da campanha 2 (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Complain | numérico | Reclamou nos últimos 2 anos (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |
| Z_CostContact | numérico | Constante (=3); significado não documentado; assumido como custo por contato (premissa P4) | 3 a 3 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original; descartada na Silver |
| Z_Revenue | numérico | Constante (=11); significado não documentado; assumido como receita por aceite (premissa P4) | 11 a 11 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original; descartada na Silver |
| Response | numérico | Aceitou a oferta da última campanha (1=sim) | 0 a 1 | Obrigatório (0 nulos) | Kaggle imakash3011/customer-personality-analysis → CSV bruto; extraído em 2026-10-21; Original |

## dim_cliente

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| cliente_id | numérico (chave) | Identificador sequencial do cliente (chave) | inteiro, 0 a 11191, únicos=2240 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: renomeado de ID |
| ano_nascimento | numérico | Ano de nascimento (corrigido se implausível) | 1940 a 1996 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Year_Birth; recalculado de idade quando corrigida (R5) |
| idade | numérico | Idade em anos na data de referência (maior data de cadastro) | 18 a 74 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: ano da data_ref − Year_Birth; >100 ou <16 → mediana (R2, R5) |
| renda | numérico | Renda anual do domicílio (imputada se nula/outlier) | 1730 a 162397 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Income; nulos e outlier → mediana por educação (R3, R4) |
| n_filhos | numérico | Total de filhos no domicílio | 0 a 3 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Kidhome + Teenhome |
| filhos_criancas | numérico | Nº de crianças no domicílio | 0 a 2 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Kidhome |
| filhos_adolescentes | numérico | Nº de adolescentes no domicílio | 0 a 2 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Teenhome |
| flag_renda_outlier | booleano | Renda original era outlier extremo | {False, True} | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver (R4) |
| flag_renda_imputada | booleano | Renda foi imputada (nula ou outlier) | {False, True} | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver (R3/R4) |
| flag_idade_corrigida | booleano | Idade foi corrigida por implausibilidade | {False, True} | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver (R5) |
| faixa_etaria | categórico | Faixa etária (até 34, 35-44, 45-54, 55-64, 65+) | 35-44; 45-54; 55-64; 65+; até 34 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: corte de idade |
| faixa_renda | categórico | Quartil de renda (Q1 menor … Q4 maior) | Q1 (menor); Q2; Q3; Q4 (maior) | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: qcut(renda, 4) |
| tem_filhos | booleano | Possui ao menos um filho no domicílio | {False, True} | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: n_filhos > 0 |

## dim_educacao

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| educacao_id | numérico (chave) | Chave substituta da dimensão educação | inteiro, 1 a 5, únicos=5 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: sequencial |
| educacao_original | categórico | Escolaridade como na origem | 2n Cycle; Basic; Graduation; Master; PhD | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Education |
| educacao | categórico | Escolaridade padronizada (Básico, Graduação, Mestrado, Doutorado) | Básico; Doutorado; Graduação; Mestrado | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: 2n Cycle e Master → Mestrado (R7) |
| educacao_nivel | numérico | Nível ordinal da escolaridade (1 a 4) | 1 a 4 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: mapeamento ordinal |

## dim_estado_civil

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| estado_civil_id | numérico (chave) | Chave substituta da dimensão estado civil | inteiro, 1 a 6, únicos=6 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: sequencial |
| estado_civil | categórico | Estado civil padronizado | Casado(a); Divorciado(a); Não informado; Solteiro(a); União estável; Viúvo(a) | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Alone→Solteiro(a); Absurd/YOLO→Não informado (R6) |
| estado_civil_grupo | categórico | Com parceiro(a) / Sem parceiro(a) / Não informado | Com parceiro(a); Não informado; Sem parceiro(a) | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver (R6) |

## dim_tempo

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| data_id | numérico (chave) | Chave da data de cadastro (aaaammdd) | inteiro, 20120730 a 20140629, únicos=663 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold: de Dt_Customer |
| data | data | Data de cadastro | 2012-07-30 a 2014-06-29 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Silver: Dt_Customer convertido (R2) |
| ano | numérico | Ano da data | 2012 a 2014 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold |
| trimestre | numérico | Trimestre da data | 1 a 4 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold |
| mes | numérico | Mês da data | 1 a 12 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold |
| dia_semana | numérico | Dia da semana (1=segunda) | 1 a 7 | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold |
| ano_mes | texto | Ano-mês (aaaa-mm) | 24 valores distintos | Obrigatório (0 nulos) | Bronze → Silver → Gold; extraído em 2026-10-21; Gold |

## dim_segmento

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| segmento_id | numérico (chave) | Segmento do cluster (1 = maior gasto médio) | inteiro, 1 a 3, únicos=3 | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold: K-Means, ordenado por gasto médio |
| rotulo | categórico | Rótulo do segmento (S1 maior gasto … Sk menor gasto) | S1 - maior gasto; S2 - gasto intermediário; S3 - menor gasto | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold |
| n_clientes | numérico | Nº de clientes no segmento | 527 a 1068 | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold: contagem |
| gasto_medio | numérico | Gasto total médio do segmento | 98.0698 a 1112.32 | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold: média |
| renda_media | numérico | Renda média do segmento | 29884.8 a 69127.3 | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold: média |
| recencia_media | numérico | Recência média (dias) do segmento | 47.4682 a 52.0304 | Obrigatório (0 nulos) | Silver → K-Means (Gold); extraído em 2026-10-21; Gold: média |

## fato_cliente_vendas

| Atributo | Tipo | Descrição | Domínio | Obrigatoriedade | Linhagem |
|---|---|---|---|---|---|
| cliente_id | numérico (chave) | Identificador sequencial do cliente (chave) | inteiro, 0 a 11191, únicos=2240 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: renomeado de ID |
| educacao_id | numérico (chave) | Chave substituta da dimensão educação | inteiro, 1 a 5, únicos=5 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Gold: sequencial |
| estado_civil_id | numérico (chave) | Chave substituta da dimensão estado civil | inteiro, 1 a 6, únicos=6 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Gold: sequencial |
| data_id | numérico (chave) | Chave da data de cadastro (aaaammdd) | inteiro, 20120730 a 20140629, únicos=663 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Gold: de Dt_Customer |
| segmento_id | numérico (chave) | Segmento do cluster (1 = maior gasto médio) | inteiro, 1 a 3, únicos=3 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Gold: K-Means, ordenado por gasto médio |
| recencia_dias | numérico | Dias desde a última compra | 0 a 99 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Recency |
| tempo_cliente_dias | numérico | Dias entre o cadastro e a data de referência | 0 a 699 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: data_ref − Dt_Customer (R2, R8) |
| gasto_total | numérico | Gasto total nas 6 categorias | 5 a 2525 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: soma de Mnt* (R8) |
| gasto_vinhos | numérico | Gasto com vinhos | 0 a 1493 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| gasto_carnes | numérico | Gasto com carnes | 0 a 1725 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| gasto_peixes | numérico | Gasto com peixes | 0 a 259 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| gasto_frutas | numérico | Gasto com frutas | 0 a 199 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| gasto_doces | numérico | Gasto com doces | 0 a 263 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| gasto_ouro | numérico | Gasto com ouro | 0 a 362 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Mnt* correspondente |
| pct_gasto_vinhos | numérico | % do gasto total em vinhos | 0 a 0.963303 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_gasto_carnes | numérico | % do gasto total em carnes | 0 a 0.99711 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_gasto_peixes | numérico | % do gasto total em peixes | 0 a 0.590909 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_gasto_frutas | numérico | % do gasto total em frutas | 0 a 0.445545 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_gasto_doces | numérico | % do gasto total em doces | 0 a 0.945848 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_gasto_ouro | numérico | % do gasto total em ouro | 0 a 0.89415 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| compras_total | numérico | Compras totais (web + catálogo + loja) | 0 a 32 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8); compras com desconto é subconjunto |
| compras_web | numérico | Compras pelo site | 0 a 27 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: NumWebPurchases |
| compras_catalogo | numérico | Compras por catálogo | 0 a 28 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: NumCatalogPurchases |
| compras_loja | numérico | Compras em loja física | 0 a 13 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: NumStorePurchases |
| compras_desconto | numérico | Compras com desconto | 0 a 15 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: NumDealsPurchases |
| visitas_web_mes | numérico | Visitas ao site no último mês | 0 a 20 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: NumWebVisitsMonth |
| ticket_medio | numérico | Gasto total ÷ compras totais (0 se sem compras) | 0 a 1679 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8, R10) |
| share_web | numérico | % das compras pelo site | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| share_catalogo | numérico | % das compras por catálogo | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| share_loja | numérico | % das compras em loja | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| pct_compras_desconto | numérico | Compras com desconto ÷ compras totais (máx. 1) | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8, R9) |
| campanha_1 | numérico | Aceitou campanha 1 | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: AcceptedCmp1 |
| campanha_2 | numérico | Aceitou campanha 2 | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: AcceptedCmp2 |
| campanha_3 | numérico | Aceitou campanha 3 | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: AcceptedCmp3 |
| campanha_4 | numérico | Aceitou campanha 4 | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: AcceptedCmp4 |
| campanha_5 | numérico | Aceitou campanha 5 | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: AcceptedCmp5 |
| campanha_ultima | numérico | Aceitou a última campanha | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Response |
| n_campanhas_aceitas | numérico | Nº de campanhas aceitas entre 1 e 5 | 0 a 4 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R8) |
| reclamacao_2anos | numérico | Reclamou nos últimos 2 anos | 0 a 1 | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver: Complain |
| flag_sem_compras | booleano | Cliente sem nenhuma compra registrada | {False, True} | Obrigatório (0 nulos) | Bronze → Silver (silver_clientes) → Gold; extraído em 2026-10-21; Silver (R10) |