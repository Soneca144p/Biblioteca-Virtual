from database import db
from models import Livro
import sqlite3


#Váriaveis globais
titulo_novo = "Cartas de Um Diabo a Seu Aprendiz"
autor_novo = "C.S. Lewis"
genero_novo = "Literatura Fantástica"
paginas_novo = 208
status_novo = "Lendo"
data_inicio_novo = "10/07/2026"


def CREATE_livro(titulo, autor, genero, paginas, status, data_inicio):
    conexao = db()
    cursor = conexao.cursor()

    if titulo == titulo_novo:
        return "Livro de mesmo titulo já criado"
    else:
        cursor.execute("""INSERT INTO livros( 
                   titulo,
                   autor,
                   genero,
                   paginas,
                   status,
                   data_inicio) VALUES (?, ?, ?, ?, ?, ?)""", (titulo, autor, genero, paginas, status, data_inicio))
        return "Livro criado com sucesso!"

    conexao.commit()
    conexao.close()

def READ_livro():
    conexao = db()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()                 #pega todos os valores puxados pelo SELECT * FROM livros e armazena na variável livros

    conexao.close()

    return [dict(livro) for livro in livros]  #transforma os dados da variavel livros em um dictionary

def EDIT_livro(idQueVouEditar: int, ColunaQueVouEditar: str, Edicao: str):
    conexao = db()
    cursor = conexao.cursor()

    colunas_disponiveis =  {
        "Titulo": "titulo",
        "Autor": "autor",
        "Gênero": "genero",
        "Paginas": "paginas",
        "Status": "status",
        "Data de Inicio": "data_inicio"
    }

    if ColunaQueVouEditar not in colunas_disponiveis:
        return "Coluna não existe ou foi escrita incorretamente"
    else:
        cursor.execute(f"""UPDATE livros SET {ColunaQueVouEditar} = ? WHERE id = ?""", (Edicao, idQueVouEditar))

        conexao.commit()
        conexao.close()
        return "Titulo alterado com sucesso"
