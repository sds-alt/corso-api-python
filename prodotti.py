cursor.execute("SELECT * FROM prodotti")
 risultato = cursor.fetchall()

 # Se vuoto lo popolo con dei dati di esempio
 if not risultato:
    lista_prodotti = [
        ("Mouse Wireless", 25.50),
        ("Tastiera Meccanica", 89.90),
        ("Monitor 24 Pollici", 149.00),
        ("Cuffie Gaming", 45.00),
        ("Tappetino XL", 15.00)
    ]
    cursor.executemany("INSERT INTO prodotti (nome, prezzo) VALUES (?, ?)", lista_prodotti)
    conn.commit()

 # Chiudiamo la connessione iniziale globale
 conn.close()
 print ("database inizializzato")