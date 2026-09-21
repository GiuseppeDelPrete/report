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


# 1) GESTIONE PARAMETRI DA RIGA DI COMANDO

parser = argparse.ArgumentParser(
    description="Generatore report misurazioni sensori."
)

parser.add_argument(
    "--output",
    type=str,
    default="report.pdf",
    help="Nome del file PDF di output"
)

parser.add_argument(
    "--data-inizio",
    type=str,
    default=None,
    help="Data di inizio nel formato YYYY-MM-DD"
)

parser.add_argument(
    "--data-fine",
    type=str,
    default=None,
    help="Data di fine nel formato YYYY-MM-DD"
)

args = parser.parse_args()


# 2) CONVERSIONE E CONTROLLO DELLE DATE

try:
    data_inizio = (
        datetime.strptime(args.data_inizio, "%Y-%m-%d").date()
        if args.data_inizio
        else None
    )

    data_fine = (
        datetime.strptime(args.data_fine, "%Y-%m-%d").date()
        if args.data_fine
        else None
    )

except ValueError:
    print("Errore: le date devono essere nel formato YYYY-MM-DD.")
    exit(1)


# Controllo che la data iniziale non sia successiva alla data finale

if data_inizio and data_fine and data_inizio > data_fine:
    print("Errore: la data di inizio non può essere successiva alla data di fine.")
    exit(1)


# 3) LETTURA DEL FILE JSON DEI SENSORI

with open(
    "sensor_measurements.json",
    "r",
    encoding="utf-8"
) as file:
    dati_json = json.load(file)


parametro = dati_json.get(
    "parameter",
    "temperature"
)

unita = dati_json.get(
    "unit",
    "°C"
)

intervallo = dati_json.get(
    "sampling_interval_minutes",
    10
)

misurazioni = dati_json.get(
    "measurements",
    []
)


# 4) FILTRO DELLE MISURAZIONI IN BASE AL PERIODO SCELTO

misurazioni_filtrate = []

for m in misurazioni:

    try:
        timestamp = datetime.fromisoformat(
            m["timestamp"].replace("Z", "+00:00")
        )

        data_misurazione = timestamp.date()

    except (KeyError, ValueError):
        print(
            f"Attenzione: timestamp non valido: "
            f"{m.get('timestamp')}"
        )
        continue

    # Se è stata specificata una data iniziale,
    # vengono escluse le misurazioni precedenti

    if data_inizio and data_misurazione < data_inizio:
        continue

    # Se è stata specificata una data finale,
    # vengono escluse le misurazioni successive

    if data_fine and data_misurazione > data_fine:
        continue

    misurazioni_filtrate.append(m)


# Controllo presenza di misurazioni

if not misurazioni_filtrate:
    print(
        "Nessuna misurazione trovata "
        "nel periodo specificato."
    )
    exit(1)


# 5) CREAZIONE DEL TITOLO

titolo = (
    f"Report Misurazioni: "
    f"{parametro.capitalize()} ({unita})"
)


# 6) ESTRAZIONE DINAMICA DEI SENSORI

timestamps = [
    mis["timestamp"]
    for mis in misurazioni_filtrate
]

sensori = sorted(
    key
    for key in misurazioni_filtrate[0]
    if key.startswith("sensor_")
)
# Individua automaticamente tutte le chiavi che iniziano con "sensor_"

print(f"Sensori rilevati: {sensori}")


# 7) CREAZIONE DEL GRAFICO

grafici_singoli = []

for sensore in sensori:

    valori = [
        mis[sensore]
        for mis in misurazioni_filtrate
    ]

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        timestamps,
        valori,
        marker="o",
        label=sensore
    )

    plt.title(
        f"Andamento {parametro} - {sensore}"
    )

    plt.xlabel(
        "Timestamp"
    )

    plt.ylabel(
        f"Valore ({unita})"
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    grafico_path = f"grafico_{sensore}.png"

    plt.savefig(
        grafico_path,
        dpi=150
    )

    plt.close()

    grafici_singoli.append(
        grafico_path
    )

# 8) CREAZIONE DEL PDF

pdf_path = args.output

documento = SimpleDocTemplate(
    pdf_path,
    pagesize=A4
)


styles = getSampleStyleSheet()

contenuto = []


# 9) TITOLO DEL REPORT

contenuto.append(
    Paragraph(
        titolo,
        styles["Title"]
    )
)


contenuto.append(
    Spacer(
        1,
        20
    )
)


# 10) DATA DI GENERAZIONE E INFORMAZIONI SUL PERIODO

data_generazione = datetime.now().strftime(
    "%d/%m/%Y %H:%M"
)

periodo_inizio = (
    data_inizio.strftime("%d/%m/%Y")
    if data_inizio
    else "Non specificata"
)

periodo_fine = (
    data_fine.strftime("%d/%m/%Y")
    if data_fine
    else "Non specificata"
)


contenuto.append(
    Paragraph(
        f"Report generato il: {data_generazione} | "
        f"Periodo: dal {periodo_inizio} al {periodo_fine} | "
        f"Intervallo campionamento: {intervallo} min",
        styles["Normal"]
    )
)


contenuto.append(
    Spacer(
        1,
        20
    )
)


# 11) INSERIMENTO DEL GRAFICO NEL PDF

contenuto.append(
    Paragraph(
        "Grafico Misurazioni Sensori",
        styles["Heading2"]
    )
)


contenuto.append(
    Spacer(
        1,
        10
    )
)


immagine = Image(
    grafico_path,
    width=500,
    height=250
)


contenuto.append(
    immagine
)


contenuto.append(
    Spacer(
        1,
        20
    )
)


# 12) CREAZIONE DELLA TABELLA

tabella_dati = [
    [
        "Timestamp",
        "Sensor 1",
        "Sensor 2"
    ]
]


for m in misurazioni_filtrate:

    tabella_dati.append(
        [
            m["timestamp"],
            str(m["sensor_1"]),
            str(m["sensor_2"])
        ]
    )


tabella = Table(
    tabella_dati
)


tabella.setStyle(
    TableStyle(
        [
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ]
    )
)


contenuto.append(
    tabella
)


# 13) GENERAZIONE DEL PDF FINALE

documento.build(
    contenuto
)


# 14) MESSAGGIO FINALE

print(
    f"Report creato con successo: {pdf_path}"
)

print(
    f"Periodo selezionato: "
    f"{periodo_inizio} - {periodo_fine}"
)

print(
    f"Misurazioni incluse: "
    f"{len(misurazioni_filtrate)}"
)