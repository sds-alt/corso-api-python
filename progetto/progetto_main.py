from fastapi import FastAPI
from .progetto_db import dbinit
# 1. Importiamo l'oggetto router dal file progetto_prodotti.py
from .progetto_prodotti import router as prodotti_router
from .progetto_utente import router as utenti_router
from .progetto_film import router as film_router
from fastapi.middleware.cors import CORSMiddleware
from .progetto_playlist import router as playlist_router

#inizializzo il DB
dbinit()


app = FastAPI()
#confidura il cors per accettare tutto
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"]
)


# 2. Agganciamo il router all'applicazione principale
app.include_router(prodotti_router)
@app.get("/")
def home():
 return {"info": "Server principale attivo"}

app.include_router(utenti_router)

app.include_router(film_router)

app.include_router(playlist_router)
