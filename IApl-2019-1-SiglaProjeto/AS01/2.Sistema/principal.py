import psycopg2
import codecs
import datetime
import random

from prestador import Prestador
from especialidade import Especialidade
from PrestadorEspecialidade import PrestadorEspecialidade

#Inicializando conexão com o banco de dados POSTGRESQL:
tamanho_codigo_prestador = 0
tamanho_nome_prestador = 0
tamanho_codigo_especialidade = 0
tamanho_descricao_especialidade = 0
now = datetime.datetime.now()
cod_pessoa = random.randint(0, 99999)

conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

def obtenha_pessoas(cur, coluna):
    cur.execute("SELECT * FROM dbo.Pessoa;")
    return [r[coluna] for r in cur.fetchall()]

def obtenha_prestadores(cur, coluna):
    cur.execute("SELECT * FROM dbo.Prestador;")
    return [r[coluna] for r in cur.fetchall()]

def obtenha_especialidades(cur, coluna):
    cur.execute("SELECT * FROM dbo.Especialidade;")
    return [r[coluna] for r in cur.fetchall()]

def obtenha_prestador_especialidade(cur, coluna):
    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
    return [r[coluna] for r in cur.fetchall()]

#Obtendo dados para a escrita no arquivo:

def obtenha_nome_prestador(cur, index):
    nome_prestador = cur.execute("SELECT nome from dbo.Prestador WHERE prestadorid = {}".format(
        obtenha_prestador_especialidade(cur, 0)[index]))
    nome_prestador = cur.fetchall()[0][0]
    global tamanho_nome_prestador
    tamanho_nome_prestador =  len(str(nome_prestador))

    return nome_prestador

def obtenha_codigo_prestador(cur, index):
    codigo_prestador = cur.execute("SELECT prestadorid from dbo.Prestador WHERE nome = '{}'".format(
        obtenha_prestadores(cur, 1)[index]))
    codigo_prestador = cur.fetchall()[0][0]
    global tamanho_codigo_prestador
    tamanho_codigo_prestador = len(str(codigo_prestador))

    return codigo_prestador

def obtenha_descricao_especialidade(cur,index):
    descricao_especialidade = cur.execute("SELECT descricao from dbo.Especialidade WHERE especialidadeid = '{}'".format(
        obtenha_prestador_especialidade(cur, 1)[index]))
    descricao_especialidade = cur.fetchall()[0][0]
    global tamanho_descricao_especialidade
    tamanho_descricao_especialidade = len(str(descricao_especialidade))

    return descricao_especialidade

def obtenha_codigo_especialidade(cur, index):
    codigo_especialidade = cur.execute("SELECT especialidadeid from dbo.Especialidade WHERE descricao = '{}'".format(
        obtenha_especialidades(cur, 1)[index]))
    codigo_especialidade = cur.fetchall()[0][0]
    global tamanho_codigo_especialidade
    tamanho_codigo_especialidade = len(str(codigo_especialidade))

    return codigo_especialidade

#Escrevendo no arquivo no formato UTF-8:

def gravar_arquivo(cur):
    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
    number_rows = cur.rowcount
    
    file = codecs.open("escrita.txt", "w", "utf-8")

    for index in range(number_rows):
        
        file.write(str(obtenha_codigo_prestador(cur, index)))
        for index2 in range(10 - tamanho_codigo_prestador):
            file.write(" ")
        file.write(obtenha_nome_prestador(cur, index))
        for index3 in range(100 - tamanho_nome_prestador):
            file.write(" ")
        file.write(str(obtenha_codigo_especialidade(cur, index)))
        for index4 in range(8 - tamanho_codigo_especialidade):
            file.write(" ")
        file.write(obtenha_descricao_especialidade(cur, index))
        for index5 in range(30 - tamanho_descricao_especialidade):
            file.write(" ")
        file.write("\n")
    
    file.close()

print("Gravando no arquivo")

gravar_arquivo(cur)

print("Arquivo gravado")


# Gravando no banco de dados:

def grave_arquivo_texto():
    num_lines = 0
    with open("escrita.txt", "r") as f:
        for line in f:
            num_lines += 1
    for index in range(num_lines):
        file = open("leitura.txt", "r")
        line = file.readline()
        cur.execute("INSERT INTO dbo.ESPECIALIDADE VALUES('{}', '{}', '{}', NULL )".format(line[110:117], line[118:139], now))
        cur.execute("INSERT INTO dbo.PRESTADOR VALUES('{}', '{}', '{}', NULL, nextval('dbo.pessoaid_seq'))".format(line[0:9], line[10:109], now))
        conn.commit()

grave_arquivo_texto()