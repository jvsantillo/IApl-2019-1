-- Criando as tabelas e fazendo uso das Sequences

CREATE TABLE dbo.Pessoa
(
    PessoaID integer NOT NULL DEFAULT NEXTVAL('dbo.pessoaid_seq'),
    Nome character varying(40) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    PRIMARY KEY (PessoaID)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Pessoa
    OWNER to postgres;

------------------------------------------------------------------------------------------------

CREATE TABLE dbo.Prestador
(
    PrestadorID integer NOT NULL DEFAULT NEXTVAL('dbo.prestadorid_seq'),
    Nome character varying(40) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    PessoaID integer NOT NULL,
    PRIMARY KEY (PessoaID, PrestadorID)
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
    IdEspecialidade integer NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,   
    PRIMARY KEY (ID, IdEspecialidade )
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Prestador_Especialidade
    OWNER to postgres;

-------------------------------------------------------------------------------------------------

CREATE TABLE dbo.Especialidade
(
    EspecialidadeID integer NOT NULL DEFAULT NEXTVAL('dbo.especialidadeid_seq'),
    Descricao character varying(80) NOT NULL,
    DataInclusao date NOT NULL,
    DataExclusao date,
    PRIMARY KEY (EspecialidadeID)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE dbo.Especialidade
    OWNER to postgres;