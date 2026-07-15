from fastapi import APIRouter, HTTPException
import sqlite3

from .progetto_classi_validazione import PlaylistIn
from .progetto_db import dbinit

dbinit()

router = APIRouter()

@router.post("/playlist")
def crea_playlist(dati: PlaylistIn, token: str):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM utenti WHERE token = ?",
        (token,)
    )

    utente = cursor.fetchone()

    if utente is None:
        conn.close()
        raise HTTPException(
            status_code=401,
            detail="Devi fare il login!"
        )

    cursor.execute(
        """
        INSERT INTO playlist_video
        (titolo_playlist, utente_id)
        VALUES (?, ?)
        """,
        (dati.titolo_playlist, utente[0])
    )

    conn.commit()
    conn.close()

    return {"messaggio": "Playlist creata"}

@router.get("/playlist")
def dammi_mie_playlist(token: str):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM utenti WHERE token = ?",
        (token,)
    )

    utente = cursor.fetchone()

    if utente is None:
        conn.close()
        raise HTTPException(
            status_code=401,
            detail="Token non valido"
        )

    cursor.execute(
        """
        SELECT id, titolo_playlist
        FROM playlist_video
        WHERE utente_id = ?
        AND film_id IS NULL
        """,
        (utente["id"],)
    )

    playlist = cursor.fetchall()

    conn.close()

    return playlist

@router.post("/playlist/aggiungi-film")
def aggiungi_film_a_lista(
    titolo_p: str,
    id_f: int,
    token: str
 ):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM utenti WHERE token = ?",
        (token,)
    )

    utente = cursor.fetchone()

    if utente is None:
        conn.close()
        raise HTTPException(
            status_code=401,
            detail="Token non valido"
        )

    cursor.execute(
        """
        INSERT INTO playlist_video
        (titolo_playlist, utente_id, film_id)
        VALUES (?, ?, ?)
        """,
        (titolo_p, utente[0], id_f)
    )

    conn.commit()
    conn.close()

    return {"messaggio": "Film aggiunto"}

@router.get("/playlist/dettaglio")
def dettaglio_playlist(
    titolo_playlist: str,
    token: str
 ):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM utenti WHERE token = ?",
        (token,)
    )

    utente = cursor.fetchone()

    if utente is None:
        conn.close()
        raise HTTPException(
            status_code=401,
            detail="Token non valido"
        )

    cursor.execute(
        """
        SELECT film.id, film.titolo
        FROM playlist_video
        JOIN film
        ON playlist_video.film_id = film.id
        WHERE playlist_video.titolo_playlist = ?
        AND playlist_video.utente_id = ?
        """,
        (titolo_playlist, utente["id"])
    )

    film = cursor.fetchall()

    conn.close()

    return film