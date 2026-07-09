# Databricks notebook source
# MAGIC %md
# MAGIC # GrowBet BI Case
# MAGIC
# MAGIC ## Notebook 01 - Ingestão
# MAGIC
# MAGIC Objetivo
# MAGIC
# MAGIC Realizar a ingestão dos arquivos CSV disponibilizados para o case,
# MAGIC criando as tabelas que serão utilizadas nas próximas etapas da análise.
# MAGIC
# MAGIC Nesta etapa não serão realizados tratamentos ou transformações.

# COMMAND ----------

vendas = spark.read.csv(
    "file:/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/vendas.csv",
    header=True,
    inferSchema=True
)

clientes = spark.read.csv(
    "file:/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/clientes.csv",
    header=True,
    inferSchema=True
)

campanhas = spark.read.csv(
    "file:/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/campanhas_serio.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

vendas.write.mode("overwrite").saveAsTable("bronze_vendas")

clientes.write.mode("overwrite").saveAsTable("bronze_clientes")

campanhas.write.mode("overwrite").saveAsTable("bronze_campanhas")