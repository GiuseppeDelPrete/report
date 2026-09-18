import json
import csv
from datetime import datetime

import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)



# 1) LETTURA DEL FILE JSON


with open("dati.json", "r", encoding="utf-8") as file:
    dati_json = json.load(file) 
                                

titolo = dati_json["titolo"] 

dati = dati_json["dati"]



# 2) LETTURA DEL FILE CSV


mesi = []
vendite = []

with open("dati.csv", "r", encoding="utf-8") as file:
    lettore = csv.DictReader(file)

    for riga in lettore:
        mesi.append(riga["mese"])
        vendite.append(int(riga["vendite"]))



# 3) CREAZIONE GRAFICO CSV


# Il metodo plt.figure() serve a creare un nuovo oggetto Figure,
# che rappresenta la finestra principale o il foglio su cui vengono posizionati uno o più grafici
plt.figure(figsize=(8, 5))

#La funzione plt.bar() in Python serve a creare un diagramma a barre verticali usando la libreria Matplotlib
plt.bar(
    mesi,
    vendite
)

plt.title("Vendite mensili")
#plt.xlabel() in Python è una funzione della libreria Matplotlib che serve a impostare il 
#testo dell'etichetta per l'asse orizzontale (asse x) di un grafico
plt.xlabel("Mese")
plt.ylabel("Vendite")

plt.tight_layout()
#plt.tight_layout() è una funzione utilizzata per ottimizzare automaticamente lo spazio tra i vari elementi di un grafico

grafico_csv = "grafico_vendite.png"

plt.savefig(
    grafico_csv,
    dpi=150
)


plt.close()


# 4) ESTRAZIONE DEI DATI X E Y DAL JSON


x = [elemento["x"] for elemento in dati]
y = [elemento["y"] for elemento in dati]




# 5. CREAZIONE DEL GRAFICO JSON


plt.figure(figsize=(10, 5))

plt.plot(
    x,
    y,
    marker="o"
)
#la funzione plt.plot prende le due liste appena estratte e le usa come coordinate geometriche per tracciare i punti sul grafico

plt.title(titolo)
plt.xlabel("X")
plt.ylabel("Y")
#plt.xlabel("X"), Matplotlib scriverà la lettera "X" sotto l'asse orizzontale

plt.grid(True) #serve a mostrare la griglia di sfondo sul grafico

plt.tight_layout()

grafico_path = "grafico.png"

plt.savefig(
    grafico_path,
    dpi=150
)

plt.close()



# 6) CREAZIONE DEL PDF


pdf_path = "report.pdf"

documento = SimpleDocTemplate(
    pdf_path,
    pagesize=A4
) 
styles = getSampleStyleSheet()

contenuto = []



# TITOLO DEL REPORT


contenuto.append(
    Paragraph(
        titolo,
        styles["Title"]
    )
)

contenuto.append(
    Spacer(1, 20)
)



# DATA DI GENERAZIONE


data_generazione = datetime.now().strftime(
    "%d/%m/%Y %H:%M"
)

contenuto.append(
    Paragraph(
        f"Report generato il: {data_generazione}",
        styles["Normal"]
    )
)

contenuto.append(
    Spacer(1, 20)
)



# 7. INSERIMENTO DEL GRAFICO JSON


contenuto.append(
    Paragraph(
        "Grafico dei dati JSON",
        styles["Heading2"]
    )
)

contenuto.append(
    Spacer(1, 10)
)

immagine = Image(
    grafico_path,
    width=500,
    height=250
)

contenuto.append(immagine)

contenuto.append(
    Spacer(1, 20)
)



# 8. INSERIMENTO DEL GRAFICO CSV


contenuto.append(
    Paragraph(
        "Grafico delle vendite mensili",
        styles["Heading2"]
    )
)

contenuto.append(
    Spacer(1, 10)
)

immagine_csv = Image(
    grafico_csv,
    width=500,
    height=250
)

contenuto.append(immagine_csv)

contenuto.append(
    Spacer(1, 20)
)



# 9. TABELLA DEI DATI JSON


tabella_dati = [["X", "Y"]]

for elemento in dati:
    tabella_dati.append([
        elemento["x"],
        elemento["y"]
    ])


tabella = Table(tabella_dati)

tabella.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("PADDING", (0, 0), (-1, -1), 6)
    ])
)

contenuto.append(tabella)


# 10. GENERAZIONE DEL PDF


documento.build(contenuto) 

print(f"Report creato: {pdf_path}")
