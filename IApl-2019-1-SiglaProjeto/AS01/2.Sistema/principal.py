import psycopg2
import codecs

from prestador import Prestador
from especialidade import Especialidade
from prestador_especialidade import Prestador_Especialidade

#Inicializando conexão com o banco de dados POSTGRESQL:

conn = psycopg2.connect("dbname=teste user=postgres password=postgres")
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
    cur.execute("SELECT * FROM dbo.Prestador_Especialidade;")
    return [r[coluna] for r in cur.fetchall()]

#Obtendo dados para a escrita no arquivo:

def obtenha_nome_prestador(cur, index):
    nome_prestador = cur.execute("SELECT pre_nome from dbo.Prestador WHERE pre_codigo = {}".format(
        obtenha_prestador_especialidade(cur, 0)[index]))
    nome_prestador = cur.fetchall()[0][0]

    return nome_prestador

def obtenha_codigo_prestador(cur, index):
    codigo_prestador = cur.execute("SELECT pre_codigo from dbo.Prestador WHERE pre_nome = '{}'".format(
        obtenha_prestadores(cur, 1)[index]))
    codigo_prestador = cur.fetchall()[0][0]

    return codigo_prestador

def obtenha_descricao_especialidade(cur,index):
    descricao_especialidade = cur.execute("SELECT esp_descricao from dbo.Especialidade WHERE esp_codigo = '{}'".format(
        obtenha_prestador_especialidade(cur, 1)[index]))
    descricao_especialidade = cur.fetchall()[0][0]

    return descricao_especialidade

def obtenha_codigo_especialidade(cur, index):
    codigo_especialidade = cur.execute("SELECT esp_codigo from dbo.Especialidade WHERE esp_descricao = '{}'".format(
        obtenha_especialidades(cur, 1)[index]))
    codigo_especialidade = cur.fetchall()[0][0]

    return codigo_especialidade

#Escrevendo no arquivo no formato UTF-8:

def gravar_arquivo(cur):
    cur.execute("SELECT * FROM dbo.Prestador_Especialidade;")
    number_rows = cur.rowcount
    
    file = codecs.open("escrita.txt", "w", "utf-8")

    for index in range(number_rows):
        
        file.write(str(obtenha_codigo_prestador(cur, index)))
        file.write("\t")
        file.write(obtenha_nome_prestador(cur, index))
        file.write("\t")
        file.write(str(obtenha_codigo_especialidade(cur, index)))
        file.write("\t")
        file.write(obtenha_descricao_especialidade(cur, index))
        file.write("\n")
    
    file.close()

print("Gravando no arquivo")

gravar_arquivo(cur)

print("Arquivo gravado")


