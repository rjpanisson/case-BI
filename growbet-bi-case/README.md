# GrowBet BI Analytics

Case técnico de Business Intelligence — análise de performance comercial (receita, canais, retenção de clientes e ROAS de campanhas) para uma empresa fictícia do setor de apostas (BET), construído com **Databricks (PySpark/Spark SQL)** para o pipeline de dados e **Power BI** para modelagem e visualização.

> Case desenvolvido para processo seletivo de Analista de Dados (Pleno). Dados fornecidos no escopo do processo; nomes de empresa e produtos são fictícios.

---

## 🖥️ O Dashboard


### Executivo
Visão gerencial resumida: KPIs principais, performance por canal, origem de lead e receita mensal.

![Executivo](images/dashboard-executivo.png)

### Analítico
Aprofundamento: receita por produto, Top 5 clientes, retenção mensal (novos vs. recorrentes), tabela consolidada de campanhas e ROAS.

![Analítico](images/dashboard-analitico.png)

---

## 🎯 Perguntas de negócio respondidas

| # | KPI | Onde está |
|---|-----|-----------|
| a | Total de faturamento e ticket médio | Executivo |
| b | Performance de vendas por canal | Executivo |
| c | Top 5 produtos e clientes por receita | Analítico |
| d | Retenção mensal (novos vs. recorrentes) | Analítico |
| e | ROAS por campanha (receita/budget) | Analítico |

## 📌 Principais achados

- **Receita bem diversificada entre canais**: os 5 canais de venda têm receita muito próxima entre si (R$ 237 Mil a R$ 275 Mil), sem dependência de um canal dominante.
- **Retenção geral de 78,52%**, com curva de maturação clara mês a mês — julho (primeiro mês da base) começa com 100% de clientes novos, e a proporção de recorrentes cresce de forma consistente até dezembro.
- **"Seasonal Promo" é a campanha mais eficiente**, não a de maior receita: com apenas R$ 15,8 Mil de budget, gerou R$ 85,2 Mil em receita (ROAS de 539%) — muito acima das demais campanhas.
- **Origem de lead equilibrada**: Inbound (32,3%), Outbound (34,0%) e Partner (33,7%) têm participação quase idêntica, sem dependência excessiva de um único modelo de aquisição.

Detalhamento completo de achados e recomendações em [`docs/GrowBet_BI_Documentacao_Case.docx`](docs/GrowBet_BI_Documentacao_Case.docx).

---

## 🏗️ Arquitetura do pipeline

```
CSV (vendas, clientes, campanhas)
        │
        ▼
   🥉 BRONZE   →  Notebook 01: ingestão bruta, sem transformação
        │
        ▼
   🔍 AUDITORIA →  Notebook 02: nulos, duplicidade, integridade referencial
        │
        ▼
   🥈 SILVER    →  Notebook 03: padronização (TRIM, ROUND)
        │
        ▼
   🥇 GOLD      →  Notebook 04: esquema estrela + dimensão calendário
        │
        ▼
   📤 EXPORT    →  Notebook 05: CSV para consumo no Power BI
        │
        ▼
   📊 POWER BI  →  Modelagem DAX + Dashboard (3 páginas)
```

Documentação técnica completa do pipeline (decisões de modelagem, resultados da auditoria de qualidade) em [`docs/GrowBet_BI_Documentacao_Databricks.docx`](docs/GrowBet_BI_Documentacao_Databricks.docx).

---

## 🗂️ Estrutura do repositório

```
├── images/                    # Prints do dashboard (Home, Executivo, Analítico)
├── sql/                       # Notebooks Databricks (Bronze → Silver → Gold → Exportação)
│   ├── 01_ingestao.py
│   ├── 02_auditoria.py
│   ├── 03_silver.py
│   ├── 04_gold.py
│   └── 05_exportacao.py
└── docs/                      # Documentação de negócio e técnica
    ├── GrowBet_BI_Documentacao_Case.docx
    └── GrowBet_BI_Documentacao_Databricks.docx
```

## ⚠️ Observações técnicas e limitações

- **Taxa de conversão**: a base fornecida contém apenas vendas já convertidas, sem registro de leads não convertidos. A métrica exibida no dashboard reflete distribuição de receita por canal/origem de lead, não conversão de funil (vendas/leads).
- **Janela temporal**: a base cobre apenas 6 meses (jul–dez/2025), o que inviabiliza comparações ano a ano. Todas as medidas de variação foram construídas como comparação mês a mês.
- **ROAS vs. ROI**: a métrica solicitada no case como "ROI (receita/budget)" corresponde tecnicamente ao conceito de **ROAS** (Return on Ad Spend). O ROI clássico descontaria o investimento do retorno: `(Receita − Budget) / Budget`. Optou-se por manter a nomenclatura tecnicamente correta no dashboard, documentando a diferença.

## 🛠️ Stack

`Databricks` · `PySpark` · `Spark SQL` · `Power BI` · `DAX`

---

Desenvolvido por **Jhonathan Panisson** — [GitHub](https://github.com/rjpanisson)
