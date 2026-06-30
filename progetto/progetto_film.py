from fastapi import APIRouter 
import sqlite3

# Creiamo il mini-gestore delle rotte
router = APIRouter()


@router.get("/film")
def lista_prodotti():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film")
    risultato = cursor.fetchall()
    conn.close()
    return risultato

@router.get("/film/ricerca")
def cerca_prodotto(keyword: str):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
    "SELECT * FROM film WHERE titolo LIKE ?",
    (f"%{keyword}%",)
    )
    risultati = cursor.fetchall()
    conn.close()
    return risultati

@router.get("/film/{id_film}")
def dettaglio_film(id_film: int):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # Ricordate sempre questo!
    cursor = conn.cursor()
    cursor.execute(
    "SELECT * FROM film WHERE id = ?",
    (id_film,)
    )
    risultati = cursor.fetchone()
    conn.close()
    return risultati
