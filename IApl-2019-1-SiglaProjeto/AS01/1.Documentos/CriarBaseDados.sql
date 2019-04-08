-- Criando a Base de Dados

CREATE DATABASE PrestadorServico
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

-- Criando o esquema 'dbo'
	
	CREATE SCHEMA dbo
    AUTHORIZATION postgres;
	
ALTER DEFAULT PRIVILEGES IN SCHEMA dbo
GRANT ALL ON TABLES TO postgres;

-- Criando as tabelas

CREATE TABLE dbo.Pessoa
(
    Pes_Codigo integer NOT NULL,
    Pes_Nome character varying(40) NOT NULL,
    Pes_Dt_Inc date NOT NULL,
    Pes_Dt_Exc date,
    PRIMARY KEY (Pes_Codigo)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Pessoa
    OWNER to postgres;
	
CREATE TABLE dbo.Prestador
(
    Pre_Codigo integer NOT NULL,
    Pre_Nome character varying(40) NOT NULL,
    Pre_Dt_Inc date NOT NULL,
    Pre_Dt_Exc date,
    Pes_Codigo integer NOT NULL,
    PRIMARY KEY (Pes_Codigo, Pre_Codigo)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Prestador
    OWNER to postgres;
	
CREATE TABLE dbo.Prestador_Especialidade
(
    Pes_Pre_Codigo integer NOT NULL,
    Pes_Esp_Codigo integer NOT NULL,
    Pes_Dt_Inc date NOT NULL,
    Pes_Dt_Exc date,   
    PRIMARY KEY (Pes_Pre_Codigo, Pes_Esp_Codigo)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Prestador_Especialidade
    OWNER to postgres;

CREATE TABLE dbo.Especialidade
(
    Esp_Codigo integer NOT NULL,
    Esp_Descricao character varying(80) NOT NULL,
    Esp_Dt_Inc date NOT NULL,
    Esp_Dt_Exc date,
    PRIMARY KEY (Esp_Codigo)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Especialidade
    OWNER to postgres;