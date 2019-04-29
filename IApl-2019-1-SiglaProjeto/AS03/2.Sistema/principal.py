import psycopg2
import codecs
import datetime
import random
import json
import lxml

import xml.etree.cElementTree as ET
from lxml import etree
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

# Criando XML

def criar_xml(cur):
    root = ET.Element("root")


    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
    number_rows = cur.rowcount

    for index in range(number_rows):
        prestador = ET.SubElement(root, "prestador")
        nome = (obtenha_nome_prestador(cur, index))
        codigo = (obtenha_codigo_prestador(cur, index))
        ET.SubElement(prestador, "prestadorId").text = str(codigo)
        ET.SubElement(prestador, "nomePrestador").text = str(nome)

    tree = ET.ElementTree(root)
    tree.write("export.xml")

    print("XML gerado")

criar_xml(cur)

# Lendo XML

def ler_xml(cur):
    tree = ET.parse('import.xml')
    root = tree.getroot()

    cur.execute("SELECT * FROM dbo.PrestadorEspecialidade;")
    number_rows = cur.rowcount

    for index in range(number_rows):
        nome = root[index][0].text
        print(nome)
        cur.execute("INSERT INTO dbo.Prestador VALUES(nextval('dbo.prestadorid_seq'), '{}', '{}', NULL, nextval('dbo.pessoaid_seq'))".format(nome, now))
        conn.commit()

        print("XML gravado na base de dados")


ler_xml(cur)