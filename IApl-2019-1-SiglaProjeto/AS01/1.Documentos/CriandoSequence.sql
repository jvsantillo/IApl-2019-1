-- Criando Sequence que será usada na tabela dbo.Pessoa

CREATE SEQUENCE dbo.pessoaid_seq
INCREMENT 1
START 1
MINVALUE 1;

ALTER SEQUENCE dbo.pessoaid_seq
    OWNER TO postgres;

-- Criando Sequence que será usada na tabela dbo.Prestador

CREATE SEQUENCE dbo.prestadorid_seq
INCREMENT 1
START 1
MINVALUE 1;

ALTER SEQUENCE dbo.prestadorid_seq
    OWNER TO postgres;

-- Criando Sequence que será usada na tabela dbo.Prestador_Especialidade

CREATE SEQUENCE dbo.prestespecialidadeid_seq
INCREMENT 1
START 1
MINVALUE 1;

ALTER SEQUENCE dbo.prestespecialidadeid_seq
    OWNER TO postgres;

-- Criando Sequence que será usada na tabela dbo.Especialidade

CREATE SEQUENCE dbo.especialidadeid_seq
INCREMENT 1
START 1
MINVALUE 1;

ALTER SEQUENCE dbo.especialidadeid_seq
    OWNER TO postgres;