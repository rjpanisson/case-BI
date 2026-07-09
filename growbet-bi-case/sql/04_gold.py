# Databricks notebook source
# MAGIC %md
# MAGIC #GrowBet BI Case
# MAGIC
# MAGIC ## Notebook 04 - Gold
# MAGIC
# MAGIC Objetivo
# MAGIC
# MAGIC Camada pronta para análises

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_fato_vendas AS
# MAGIC SELECT
# MAGIC     id_venda,
# MAGIC     data,
# MAGIC     cliente_id,
# MAGIC     campanha_id,
# MAGIC     produto,
# MAGIC     canal,
# MAGIC     lead_source,
# MAGIC     valor
# MAGIC FROM silver_vendas;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_dim_clientes AS
# MAGIC SELECT
# MAGIC     cliente_id,
# MAGIC     nome,
# MAGIC     regiao,
# MAGIC     status,
# MAGIC     data_cadastro
# MAGIC FROM silver_clientes;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_dim_campanhas AS
# MAGIC SELECT
# MAGIC     campanha_id,
# MAGIC     nome,
# MAGIC     canal,
# MAGIC     budget,
# MAGIC     data_inicio
# MAGIC FROM silver_campanhas;    
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE gold_dim_data AS
# MAGIC
# MAGIC WITH calendario AS (
# MAGIC SELECT explode(
# MAGIC     sequence(
# MAGIC         TO_DATE('2025-07-01'),
# MAGIC         TO_DATE('2025-12-31'),
# MAGIC         INTERVAL 1 DAY
# MAGIC     )
# MAGIC ) AS data
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     data,
# MAGIC         YEAR(data) AS ano,
# MAGIC     CASE
# MAGIC         WHEN MONTH(data) <= 6 THEN 1
# MAGIC         ELSE 2
# MAGIC     END AS semestre,
# MAGIC
# MAGIC     QUARTER(data) AS trimestre,
# MAGIC     CONCAT('Q', QUARTER(data)) AS trimestre_nome,
# MAGIC     MONTH(data) AS mes_numero,
# MAGIC     CASE MONTH(data)
# MAGIC         WHEN 1 THEN 'Janeiro'
# MAGIC         WHEN 2 THEN 'Fevereiro'
# MAGIC         WHEN 3 THEN 'Março'
# MAGIC         WHEN 4 THEN 'Abril'
# MAGIC         WHEN 5 THEN 'Maio'
# MAGIC         WHEN 6 THEN 'Junho'
# MAGIC         WHEN 7 THEN 'Julho'
# MAGIC         WHEN 8 THEN 'Agosto'
# MAGIC         WHEN 9 THEN 'Setembro'
# MAGIC         WHEN 10 THEN 'Outubro'
# MAGIC         WHEN 11 THEN 'Novembro'
# MAGIC         WHEN 12 THEN 'Dezembro'
# MAGIC     END AS mes,
# MAGIC
# MAGIC     CONCAT(
# MAGIC         CASE MONTH(data)
# MAGIC             WHEN 1 THEN 'Jan'
# MAGIC             WHEN 2 THEN 'Fev'
# MAGIC             WHEN 3 THEN 'Mar'
# MAGIC             WHEN 4 THEN 'Abr'
# MAGIC             WHEN 5 THEN 'Mai'
# MAGIC             WHEN 6 THEN 'Jun'
# MAGIC             WHEN 7 THEN 'Jul'
# MAGIC             WHEN 8 THEN 'Ago'
# MAGIC             WHEN 9 THEN 'Set'
# MAGIC             WHEN 10 THEN 'Out'
# MAGIC             WHEN 11 THEN 'Nov'
# MAGIC             WHEN 12 THEN 'Dez'
# MAGIC         END,
# MAGIC
# MAGIC         '/',
# MAGIC         YEAR(data)
# MAGIC     ) AS mes_ano,
# MAGIC
# MAGIC     (YEAR(data) * 100) + MONTH(data) AS ano_mes_ordem,
# MAGIC     DAY(data) AS dia,
# MAGIC     WEEKOFYEAR(data) AS semana_ano,
# MAGIC     CASE
# MAGIC         WHEN DAYOFWEEK(data)=2 THEN 1
# MAGIC         WHEN DAYOFWEEK(data)=3 THEN 2
# MAGIC         WHEN DAYOFWEEK(data)=4 THEN 3
# MAGIC         WHEN DAYOFWEEK(data)=5 THEN 4
# MAGIC         WHEN DAYOFWEEK(data)=6 THEN 5
# MAGIC         WHEN DAYOFWEEK(data)=7 THEN 6
# MAGIC         WHEN DAYOFWEEK(data)=1 THEN 7
# MAGIC     END AS dia_semana_ordem,
# MAGIC     CASE            
# MAGIC         WHEN DAYOFWEEK(data)=2 THEN 'Segunda'
# MAGIC         WHEN DAYOFWEEK(data)=3 THEN 'Terça'
# MAGIC         WHEN DAYOFWEEK(data)=4 THEN 'Quarta'
# MAGIC         WHEN DAYOFWEEK(data)=5 THEN 'Quinta'
# MAGIC         WHEN DAYOFWEEK(data)=6 THEN 'Sexta'
# MAGIC         WHEN DAYOFWEEK(data)=7 THEN 'Sábado'
# MAGIC         WHEN DAYOFWEEK(data)=1 THEN 'Domingo'
# MAGIC     END AS dia_semana,
# MAGIC     CASE
# MAGIC         WHEN DAYOFWEEK(data) IN (1,7)
# MAGIC         THEN TRUE
# MAGIC         ELSE FALSE
# MAGIC     END AS fim_de_semana,
# MAGIC     DATE_TRUNC('MONTH', data) AS inicio_mes,
# MAGIC     LAST_DAY(data) AS fim_mes
# MAGIC FROM calendario
# MAGIC
# MAGIC ORDER BY data;