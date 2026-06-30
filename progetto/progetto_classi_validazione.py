from pydantic import BaseModel
class ProdottoIn(BaseModel):
    nome: str
    prezzo: float

class utente(BaseModel):
    username: str
    password_hash: str

class filmIN(BaseModel):
            titolo: str
            trama: str 
            anno: int
            url_locandina: str
            tmdb_id: str