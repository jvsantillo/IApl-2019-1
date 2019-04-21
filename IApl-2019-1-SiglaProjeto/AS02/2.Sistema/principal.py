    
import psycopg2
import codecs
import datetime
import random
import json

from prestador import Prestador
from especialidade import Especialidade
from prestador_especialidade import Prestador_Especialidade

#Inicializando conexão com o banco de dados POSTGRESQL:
tamanho_codigo_prestador = 0
tamanho_nome_prestador = 0
tamanho_codigo_especialidade = 0
tamanho_descricao_especialidade = 0
now = datetime.datetime.now()
cod_pessoa = random.randint(0, 99999)

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
    global tamanho_nome_prestador
    tamanho_nome_prestador =  len(str(nome_prestador))

    return nome_prestador

def obtenha_codigo_prestador(cur, index):
    codigo_prestador = cur.execute("SELECT pre_codigo from dbo.Prestador WHERE pre_nome = '{}'".format(
        obtenha_prestadores(cur, 1)[index]))
    codigo_prestador = cur.fetchall()[0][0]
    global tamanho_codigo_prestador
    tamanho_codigo_prestador = len(str(codigo_prestador))

    return codigo_prestador

def obtenha_descricao_especialidade(cur,index):
    descricao_especialidade = cur.execute("SELECT esp_descricao from dbo.Especialidade WHERE esp_codigo = '{}'".format(
        obtenha_prestador_especialidade(cur, 1)[index]))
    descricao_especialidade = cur.fetchall()[0][0]
    global tamanho_descricao_especialidade
    tamanho_descricao_especialidade = len(str(descricao_especialidade))

    return descricao_especialidade

def obtenha_codigo_especialidade(cur, index):
    codigo_especialidade = cur.execute("SELECT esp_codigo from dbo.Especialidade WHERE esp_descricao = '{}'".format(
        obtenha_especialidades(cur, 1)[index]))
    codigo_especialidade = cur.fetchall()[0][0]
    global tamanho_codigo_especialidade
    tamanho_codigo_especialidade = len(str(codigo_especialidade))

    return codigo_especialidade

#Escrevendo no arquivo no formato UTF-8:

def gravar_arquivo(cur):
    cur.execute("SELECT * FROM dbo.Prestador_Especialidade;")
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
    
    file.close()

print("Gravando no arquivo")

gravar_arquivo(cur)

print("Arquivo gravado")


# Gravando do arquivo de texto posicional para o banco de dados:

def grave_arquivo_texto():
    num_lines = 0
    with open("escrita.txt", "r") as f:
        for line in f:
            num_lines += 1
    for index in range(num_lines):
        file = open("leitura.txt", "r")
        line = file.readline()
        cur.execute("INSERT INTO dbo.ESPECIALIDADE VALUES('{}', '{}', '{}', NULL )".format(line[110:117], line[118:139], now))
        cur.execute("INSERT INTO dbo.PRESTADOR VALUES('{}', '{}', '{}', NULL, '{}')".format(line[0:9], line[10:109], now, cod_pessoa))
        conn.commit()

grave_arquivo_texto()

#Montando arquivo JSON:

def gerar_json(cur):
    cur.execute("SELECT * FROM dbo.Prestador_Especialidade;")
    number_rows = cur.rowcount

    codigo_prestador = []
    nome_prestador = []
    codigo_especialidade = []
    descricao_especialidade = []

    for index in range(number_rows):
    
        #Montando dict que será convertido para um objeto JSON:
        codigo_prestador.append(str(obtenha_codigo_prestador(cur, index)))
        nome_prestador.append(obtenha_nome_prestador(cur, index))
        codigo_especialidade.append(str(obtenha_codigo_especialidade(cur, index)))
        descricao_especialidade.append(obtenha_descricao_especialidade(cur, index))

    dict_json = {
        "codigo_prestadores": codigo_prestador,
        "nome_prestadores": nome_prestador,
        "codigo_especialidades": codigo_especialidade,
        "descricao_especialidades" : descricao_especialidade
    }

        json_object = json.dumps(dict_json)
    
    print(json_object)

print("Gerando JSON")
gerar_json(cur)

#Lendo JSON e gravando no banco:
def lendo_json(path_file):
    with open(path_file) as json_file:
        json_dict = json.load(json_file)

    codigo_prestadores = json_dict["codigo_prestadores"]
    nome_prestadores = json_dict["nome_prestadores"]
    codigo_especialidades = json_dict["codigo_especialidades"]
    descricao_especialidades = json_dict["descricao_especialidades"]

    for codigo_prestador, nome_prestador, codigo_especialidade, descricao_especialidade in zip(codigo_prestadores, nome_prestadores, codigo_especialidades, descricao_especialidades):
        cur.execute("INSERT INTO dbo.ESPECIALIDADE VALUES('{}', '{}', '{}', NULL )".format(codigo_especialidade, descricao_especialidade, now))
        cur.execute("INSERT INTO dbo.PRESTADOR VALUES('{}', '{}', '{}', NULL, '{}')".format(codigo_prestador, nome_prestador, now, cod_pessoa))
        conn.commit()

lendo_json('json.txt')




