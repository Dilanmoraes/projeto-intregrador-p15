# Pipeline End-to-End de Engenharia de Dados e Machine Learning

> **Projeto Integrador — Entrega Final (P15)**

## 📌 Descrição do Projeto
Pipeline completo de engenharia de dados e aprendizagem automática para previsão de *churn* de clientes.

## 🛠️ Tecnologias
- Python 3.11+
- PostgreSQL
- Scikit-Learn / Pandas

## 🚀 Como Executar
1. Execute os scripts DDL da pasta `sql/schema.sql` no seu servidor PostgreSQL.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o ETL: `python src/etl.py`
4. Execute o notebook `notebooks/pipeline_final.ipynb` para treinar e avaliar o modelo.