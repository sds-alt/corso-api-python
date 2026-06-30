import hashlib
import secrets
from fastapi import APIRouter
import sqlite3
from .progetto_classi_validazione import utente
from .progetto_db import dbinit
dbinit()

router = APIRouter()





def  calcola_hash(password_chiaro: str):
    hash_risultato = hashlib.sha256(password_chiaro.encode('utf-8')).hexdigest()
    return hash_risultato


@router.post("/register")
def registra_utente(dati: utente):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO utenti (username, password_hash) VALUES (?, ?)", (dati.username, dati.password_hash))
    conn.commit()
    conn.close()
    return{"bravo"}

@router.post("/login")
def crea_prodotto(dati: utente):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM utenti WHERE username = ?", (dati.username,))
    utente = cursor.fetchone()
    token_sessione = secrets.token_hex(16)
    cursor.execute("UPDATE utenti SET token = ? WHERE id = ?", (token_sessione, utente[0]))
    conn.commit()
    conn.close()
    return {"token": token_sessione}
    

    

    

    


