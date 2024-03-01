# Ordina Foto
Permette di dividere le foto e video in cartelle in base all'anno, mese, settimana ottenuti dal takeout di Google Foto.

In particolare utilizza i file json associati al rispettivo file jpeg, jpg o mp4 per ottenere le informazioni di creazione del contenuto

# Come utilizzare
Sostituire le variabili:
- `BASE_DIR` con il path assoluto della cartella che contiene tutte le cartelle con le foto e video
- `SPECIAL_DIR` con il path assoluto della cartella che contiene le foto o video che non sono associati a nessun file json
- `NEW_DIR` con il nome della nuova cartella che si vuole ottenere
Una volta fatto quanto sopra, scrivere nel terminale il comando `python3 ordinaFoto.py`
