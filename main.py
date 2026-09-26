from fastapi import FastAPI
from crud import READ_livro, CREATE_livro, EDIT_livro
from models import Livro
from crud import titulo_novo, autor_novo


app = FastAPI()

@app.get("/livros")
def Call_Read_livros():
    return READ_livro()

@app.post("/livros")
def Call_Create_livro():
    return(CREATE_livro(
        titulo_novo,
        autor_novo,
        "Literatura Fantástica",
        208,
        "Lendo",
        "10/07/2026"
    ))

@app.put("/livros")
def Call_Edit_livro():
    return EDIT_livro(2, "Titulo", "ADMIRÁVEL MUNDO NOVO")