# Databricks notebook source
# MAGIC %md
# MAGIC #GrowBet BI Case
# MAGIC
# MAGIC ##Notebook 05 -Exportação
# MAGIC
# MAGIC Objetivo
# MAGIC
# MAGIC Exportat as tabelas Gold .CSV para uso no Power BI
# MAGIC
# MAGIC Abordagem foi adotada para tornar a solução totalmente reproduzível e facilitar a avaliação técnica sem dependência de credenciais ou infraestrutura externa.

# COMMAND ----------

import pandas as pd

spark.table("gold_fato_vendas").toPandas().to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_fato_vendas.csv",
    index=False,
    encoding="utf-8-sig"
)

spark.table("gold_dim_clientes").toPandas().to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_dim_clientes.csv",
    index=False,
    encoding="utf-8-sig"
)

spark.table("gold_dim_campanhas").toPandas().to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_dim_campanhas.csv",
    index=False,
    encoding="utf-8-sig"
)

spark.table("gold_dim_data").toPandas().to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_dim_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivos exportados com sucesso.")

# COMMAND ----------

import pandas as pd

df = spark.table("gold_fato_vendas").toPandas()

df["valor"] = df["valor"].astype(float).round(2)

df.to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_fato_vendas.csv",
    index=False,
    sep=",",
    decimal=".",
    float_format="%.2f",
    encoding="utf-8-sig"
)

# COMMAND ----------

import pandas as pd

spark.table("gold_dim_data").toPandas().to_csv(
    "/Workspace/Users/panissoon@outlook.com/GrowBet BI Case/gold_dim_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivos exportados com sucesso.")