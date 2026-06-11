import sqlite3
from fastapi import FastAPI

app = FastAPI()

#@app.get("/utente")
#def root():
   # return {"nome": "stefano", "cognome":"di silvestre"}

@app.get("/saluta/{nome}")
def saluta_utente(nome:str):
    return {"messaggio":f"ciao (nome)!"}
#/saluta/carlo

@app.get("/ricerca")
def cerca(item:str,q:int =1):
    return {"risultato":item,"quantita":q}
#/ricerca?item=mela&q=5

@app.get("/somma/{n1}/{n2}")
def cerca(n1:int = 1,n2:int =1):
    if n1==1 and n2==1:
            return "raise httpexception(status_code=404, detail=operazione non valida)"
    return {"risultato":f"{n1+n2}"}

@app.get("/prodotti")
def ottieni_prodotti():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # Conversione attiva!
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prodotti")
    risultato = cursor.fetchall()
    conn.close()
    return risultato

@app.get("/prodotti/ricerca")
def cerca_prodotto(keyword: str):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
    "SELECT * FROM prodotti WHERE nome LIKE ?",
     (f"%{keyword}%",)
    )
    risultati = cursor.fetchall()
    conn.close()
    return risultati

#/somma/10/10