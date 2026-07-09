# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC # GrowBet BI Case
# MAGIC
# MAGIC ## Notebook 02 - Auditoria dos Dados (Qualidade)
# MAGIC
# MAGIC Objetivo
# MAGIC
# MAGIC - Verificação de registros duplicados: nenhuma duplicidade encontrada.
# MAGIC - Verificação de valores nulos: nenhum campo crítico apresentou valores ausentes.
# MAGIC - Verificação de integridade referencial entre vendas, clientes e campanhas: nenhuma inconsistência encontrada.
# MAGIC - Tipagem dos dados validada durante a ingestão.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM bronze_vendas

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM bronze_campanhas

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT (*) FROM bronze_clientes

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     SUM(CASE 
# MAGIC             WHEN cliente_id IS NULL THEN 1 ELSE 0 
# MAGIC         END) cliente_id_null,
# MAGIC     SUM(CASE 
# MAGIC             WHEN campanha_id IS NULL THEN 1 ELSE 0 
# MAGIC         END) campanha_id_null,
# MAGIC     SUM(CASE 
# MAGIC             WHEN valor IS NULL THEN 1 ELSE 0 
# MAGIC         END) valor_null
# MAGIC FROM bronze_vendas;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     id_venda,
# MAGIC     COUNT(*)
# MAGIC FROM bronze_vendas
# MAGIC GROUP BY id_venda
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     cliente_id,
# MAGIC     COUNT(*)
# MAGIC FROM bronze_clientes
# MAGIC GROUP BY cliente_id
# MAGIC HAVING COUNT(*) > 1;
# MAGIC     
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     campanha_id,
# MAGIC     COUNT(*)
# MAGIC FROM bronze_campanhas
# MAGIC GROUP BY campanha_id
# MAGIC HAVING COUNT(*) > 1;
# MAGIC     

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze_vendas v 
# MAGIC LEFT JOIN bronze_clientes c 
# MAGIC ON v.cliente_id = c.cliente_id
# MAGIC WHERE c.cliente_id IS NULL;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze_vendas v 
# MAGIC LEFT JOIN bronze_campanhas camp 
# MAGIC ON v.campanha_id = camp.campanha_id
# MAGIC WHERE camp.campanha_id IS NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     MIN (valor),
# MAGIC     MAX (valor),
# MAGIC     AVG (valor)
# MAGIC FROM bronze_vendas;