--Populando a tabela dbo.Pessoa

INSERT INTO dbo.Pessoa (Nome, DataInclusao, DataExclusao)
VALUES ('Sérgio Pedro Henrique', '11-02-2003', NULL);

INSERT INTO dbo.Pessoa (Nome, DataInclusao, DataExclusao)
VALUES ('Ana Cristina Souza', '19-06-2015', '28-12-2017');

INSERT INTO dbo.Pessoa (Nome, DataInclusao, DataExclusao)
VALUES ('Mariane Valentina da Costa', '04-07-1997', NULL);

INSERT INTO dbo.Pessoa (Nome, DataInclusao, DataExclusao)
VALUES ('Paulo Carvalho', '21-01-2019', NULL);

INSERT INTO dbo.Pessoa (Nome, DataInclusao, DataExclusao)
VALUES ('Marcos Antonio Rabelo', '08-09-1999', '10-01-2018');

-- Populando a tabela dbo.Prestador

INSERT INTO dbo.Prestador (Nome, DataInclusao, DataExclusao, Pessoa_ID)
VALUES ('Ana Cristina Souza', '28-10-2016', '28-12-2017', 1);

INSERT INTO dbo.Prestador (Nome, DataInclusao, DataExclusao, Pessoa_ID)
VALUES ('Paulo Carvalho', '22-01-2019', NULL, 2);

INSERT INTO dbo.Prestador (Nome, DataInclusao, DataExclusao, Pessoa_ID)
VALUES ('Sérgio Pedro Henrique', '18-02-2003', NULL, 3);

INSERT INTO dbo.Prestador (Nome, DataInclusao, DataExclusao, Pessoa_ID)
VALUES ('Marcos Antonio Rabelo', '20-12-2008', '10-01-2018', 4);

-- Populando a tabela dbo.Prestador_Especialidade

INSERT INTO dbo.Prestador_Especialidade (ID_Especialidade, DataInclusao, DataExclusao)
VALUES (1, '28-10-2016', NULL);

INSERT INTO dbo.Prestador_Especialidade (ID_Especialidade, DataInclusao, DataExclusao)
VALUES (2, '22-01-2019', NULL);

INSERT INTO dbo.Prestador_Especialidade (ID_Especialidade, DataInclusao, DataExclusao)
VALUES (3, '18-02-2003', '25-04-2010');

INSERT INTO dbo.Prestador_Especialidade (ID_Especialidade, DataInclusao, DataExclusao)
VALUES (4, '20-12-2008', '10-01-2018');

-- Populando a tabela dbo.Especialidade

INSERT INTO dbo.Especialidade (Descricao, DataInclusao, DataExclusao)
VALUES ('Cardiologia', '10-04-2004', NULL);

INSERT INTO dbo.Especialidade (Descricao, DataInclusao, DataExclusao)
VALUES ('Cirurgiao Geral', '28-08-1956', NULL);

INSERT INTO dbo.Especialidade (Descricao, DataInclusao, DataExclusao)
VALUES ('Esteticista de Estilo', '21-07-1980', '21-07-1981');

INSERT INTO dbo.Especialidade (Descricao, DataInclusao, DataExclusao)
VALUES ('Medico de Rede Social', '01-03-2016', '25-07-2018');

INSERT INTO dbo.Especialidade (Descricao, DataInclusao, DataExclusao)
VALUES ('Pediatria', '24-03-1959', NULL);