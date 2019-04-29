import psycopg2
import codecs
import datetime
import random
import json

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

def obtenha_PrestadorEspecialidade(cur, coluna):
    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
    return [r[coluna] for r in cur.fetchall()]

#Obtendo dados para a escrita no arquivo:

def obtenha_nome_prestador(cur, index):
    nome_prestador = cur.execute("SELECT nome from dbo.Prestador WHERE prestadorid = {}".format(
        obtenha_PrestadorEspecialidade(cur, 0)[index]))
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
        obtenha_PrestadorEspecialidade(cur, 1)[index]))
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


#Montando arquivo JSON:

def gerar_json(cur):
    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
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
        cur.execute("INSERT INTO dbo.ESPECIALIDADE VALUES(nextval('dbo.especialidadeid_seq'), '{}', '{}', NULL )".format(descricao_especialidade, now))
        cur.execute("INSERT INTO dbo.PRESTADOR VALUES(nextval('dbo.prestadorid_seq'), '{}', '{}', NULL, nextval('dbo.pessoaid_seq'))".format(nome_prestador, now))
        conn.commit()

lendo_json('json.txt')

