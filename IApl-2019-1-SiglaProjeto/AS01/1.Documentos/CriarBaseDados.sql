-- Criando as tabelas e fazendo uso das Sequences

CREATE TABLE dbo.Pessoa
(
    Pessoa_ID integer NOT NULL DEFAULT NEXTVAL('dbo.pessoaid_seq'),
    Nome character varying(40) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    PRIMARY KEY (Pessoa_ID)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Pessoa
    OWNER to postgres;

------------------------------------------------------------------------------------------------

CREATE TABLE dbo.Prestador
(
    Prestador_ID integer NOT NULL DEFAULT NEXTVAL('dbo.prestadorid_seq'),
    Nome character varying(40) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    Pessoa_ID integer NOT NULL,
    PRIMARY KEY (Pessoa_ID, Prestador_ID)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Prestador
    OWNER to postgres;

------------------------------------------------------------------------------------------------

CREATE TABLE dbo.Prestador_Especialidade
(
    ID integer NOT NULL DEFAULT NEXTVAL('dbo.prestespecialidadeid_seq'),
    ID_Especialidade integer NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,   
    PRIMARY KEY (ID, ID_Especialidade )
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Prestador_Especialidade
    OWNER to postgres;

-------------------------------------------------------------------------------------------------

CREATE TABLE dbo.Especialidade
(
    Especialidade_ID integer NOT NULL DEFAULT NEXTVAL('dbo.especialidadeid_seq'),
    Descricao character varying(80) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    PRIMARY KEY (Especialidade_ID)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Especialidade
    OWNER to postgres;