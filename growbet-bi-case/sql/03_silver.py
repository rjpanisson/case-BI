# Databricks notebook source
# MAGIC %md
# MAGIC #GrowBet BI Case
# MAGIC
# MAGIC ## Notebook 03 - Silver
# MAGIC
# MAGIC Objetivo
# MAGIC
# MAGIC Camada responsável por padronizar os dados e limpar os espaços.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver_vendas AS
# MAGIC SELECT
# MAGIC     id_venda,
# MAGIC     data,
# MAGIC     cliente_id,
# MAGIC     campanha_id,
# MAGIC     TRIM (produto) AS produto,
# MAGIC     TRIM (canal) AS canal,
# MAGIC     TRIM (lead_source) AS lead_source,
# MAGIC     ROUND(valor,2) AS valor
# MAGIC FROM bronze_vendas;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver_clientes AS
# MAGIC SELECT
# MAGIC     cliente_id,
# MAGIC     TRIM (nome) AS nome,
# MAGIC     TRIM (regiao) AS regiao,
# MAGIC     TRIM (status) AS status,
# MAGIC     data_cadastro
# MAGIC FROM bronze_clientes;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver_campanhas AS
# MAGIC SELECT
# MAGIC     campanha_id,
# MAGIC     TRIM (nome) AS nome,
# MAGIC     TRIM (canal) AS canal,
# MAGIC     ROUND (budget, 2) AS budget,
# MAGIC     data_inicio
# MAGIC FROM bronze_campanhas;
# MAGIC