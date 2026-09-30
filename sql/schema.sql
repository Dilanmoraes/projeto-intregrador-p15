-- sql/schema.sql

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente VARCHAR(50) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50),
    estado VARCHAR(2),
    data_cadastro DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS vendas (
    id_venda VARCHAR(50) PRIMARY KEY,
    id_cliente VARCHAR(50) REFERENCES clientes(id_cliente),
    data_venda TIMESTAMP NOT NULL,
    valor_total NUMERIC(10, 2) NOT NULL,
    quantidade_itens INT NOT NULL,
    categoria_produto VARCHAR(50) NOT NULL
);