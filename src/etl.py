# src/etl.py
import pandas as pd
import json
from sqlalchemy import create_engine

# Ajusta com os dados da tua conexão local do PostgreSQL
DATABASE_URL = "postgresql://postgres:senha@localhost:5432/projeto_p15"
engine = create_engine(DATABASE_URL)

def extract():
    print("A extrair dados...")
    df_vendas = pd.read_csv("data/fonte_1_vendas.csv")
    
    with open("data/fonte_2_clientes.json", "r", encoding="utf-8") as f:
        data_clientes = json.load(f)
    df_clientes = pd.DataFrame(data_clientes)
    
    return df_vendas, df_clientes

def transform(df_vendas, df_clientes):
    print("A transformar dados...")
    df_clientes['data_cadastro'] = pd.to_datetime(df_clientes['data_cadastro']).dt.date
    df_clientes.drop_duplicates(subset=['id_cliente'], inplace=True)
    
    df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
    df_vendas['valor_total'] = pd.to_numeric(df_vendas['valor_total'], errors='coerce')
    df_vendas.dropna(subset=['id_venda', 'id_cliente', 'valor_total'], inplace=True)
    
    return df_vendas, df_clientes

def load(df_vendas, df_clientes):
    print("A carregar no PostgreSQL...")
    df_clientes.to_sql("clientes", con=engine, if_exists="append", index=False)
    df_vendas.to_sql("vendas", con=engine, if_exists="append", index=False)
    print("ETL concluído com sucesso!")

if __name__ == "__main__":
    vendas, clientes = extract()
    vendas_clean, clientes_clean = transform(vendas, clientes)
    load(vendas_clean, clientes_clean)