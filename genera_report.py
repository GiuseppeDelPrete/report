import argparse
import json
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

# 1) GESTIONE PARAMETRI DA RIGA DI COMANDO (con data inizio e fine)
parser = argparse.ArgumentParser(description="Generatore report misurazioni sensori.")
parser.add_argument("--output", type=str, default="report.pdf", help="Nome del file PDF di output")
parser.add_argument("--data-inizio", type=str, default="Non specificata", help="Data di inizio (es. 2026-06-01)")
parser.add_argument("--data-fine", type=str, default="Non specificata", help="Data di fine (es. 2026-06-30)")
args = parser.parse_args()

pdf_path = args.output
data_inizio = args.data_inizio
data_fine = args.data_fine

# 2) LETTURA DEL FILE JSON DEI SENSORI
with open("sensor_measurements.json", "r", encoding="utf-8") as file:
    dati_json = json.load(file) 

parametro = dati_json.get("parameter", "temperature")
unita = dati_json.get("unit", "°C")
intervallo = dati_json.get("sampling_interval_minutes", 10)
misurazioni = dati_json.get("measurements", [])

titolo = f"Report Misurazioni: {parametro.capitalize()} ({unita})"

# 3) ESTRAZIONE DEI DATI (Timestamp, Sensor 1 e Sensor 2)
timestamps = [m["timestamp"] for m in misurazioni]
sensor_1_valori = [m["sensor_1"] for m in misurazioni]
sensor_2_valori = [m["sensor_2"] for m in misurazioni]

# 4) CREAZIONE DEL GRAFICO PER I SENSORI
plt.figure(figsize=(10, 5))

plt.plot(
    timestamps,
    sensor_1_valori,
    marker="o",
    label="Sensor 1"
)

plt.plot(
    timestamps,
    sensor_2_valori,
    marker="s",
    label="Sensor 2"
)

plt.title(f"Andamento {parametro} ({unita})")
plt.xlabel("Timestamp")
plt.ylabel(f"Valore ({unita})")

plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.legend()

plt.tight_layout()

grafico_path = "grafico.png"

plt.savefig(
    grafico_path,
    dpi=150
)

plt.close()

# 5) CREAZIONE DEL PDF
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

# DATA DI GENERAZIONE E INFO SULLE DATE SCELTE
data_generazione = datetime.now().strftime(
    "%d/%m/%Y %H:%M"
)

contenuto.append(
    Paragraph(
        f"Report generato il: {data_generazione} | Periodo: dal {data_inizio} al {data_fine}",
        styles["Normal"]
    )
)

contenuto.append(
    Spacer(1, 20)
)

# 6) INSERIMENTO DEL GRAFICO NEL PDF
contenuto.append(
    Paragraph(
        "Grafico Misurazioni Sensori",
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

# 7) TABELLA DEI DATI DELLE MISURAZIONI
tabella_dati = [["Timestamp", "Sensor 1", "Sensor 2"]]

for m in misurazioni:
    tabella_dati.append([
        m["timestamp"],
        str(m["sensor_1"]),
        str(m["sensor_2"])
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

# 8) GENERAZIONE DEL PDF FINALE
documento.build(contenuto) 

print(f"Report creato con successo: {pdf_path} (Periodo: {data_inizio} - {data_fine})")