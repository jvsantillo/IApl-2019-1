--Populando a tabela dbo.Especialidade

INSERT INTO dbo.Especialidade
VALUES (1, 'Cardiologia', '10-04-2004', NULL);

INSERT INTO dbo.Especialidade
VALUES (2, 'Cirurgiao Geral', '28-08-1956', NULL);

INSERT INTO dbo.Especialidade
VALUES (3, 'Esteticista de Estilo', '21-07-1980', '21-07-1981');

INSERT INTO dbo.Especialidade
VALUES (4, 'Medico de Rede Social', '01-03-2016', '25-07-2018');

INSERT INTO dbo.Especialidade
VALUES (5, 'Pediatria', '24-03-1959', NULL);

--Populando a tabela dbo.Pessoa

INSERT INTO dbo.Pessoa
VALUES (1, 'Sérgio Pedro Henrique', '11-02-2003', NULL)

INSERT INTO dbo.Pessoa
VALUES (2, 'Ana Cristina Souza', '19-06-2015', '28-12-2017')

INSERT INTO dbo.Pessoa
VALUES (3, 'Mariane Valentina da Costa', '04-07-1997', NULL)

INSERT INTO dbo.Pessoa
VALUES (4, 'Paulo Carvalho', '21-01-2019', NULL)

INSERT INTO dbo.Pessoa
VALUES (5, 'Marcos Antonio Rabelo', '08-09-1999', '10-01-2018')

-- Populando a tabela dbo.Prestador

INSERT INTO dbo.Prestador
VALUES (1, 'Ana Cristina Souza', '28-10-2016', ''28-12-2017);

INSERT INTO dbo.Prestador
VALUES (2, 'Paulo Carvalho', '22-01-2019', NULL);

INSERT INTO dbo.Prestador
VALUES (3, 'Sérgio Pedro Henrique', '18-02-2003', NULL);

INSERT INTO dbo.Prestador
VALUES (4, 'Marcos Antonio Rabelo', '20-12-2008', '10-01-2018');

-- Populando a tabela dbo.Prestador_Especialidade

INSERT INTO dbo.Prestador_Especialidade
VALUES (1, 1, '28-10-2016', NULL);

INSERT INTO dbo.Prestador_Especialidade
VALUES (2, 2, '22-01-2019', NULL);

INSERT INTO dbo.Prestador_Especialidade
VALUES (3, 3, '18-02-2003', '25-04-2010');

INSERT INTO dbo.Prestador_Especialidade
VALUES (4, 4, '20-12-2008', '10-01-2018');

