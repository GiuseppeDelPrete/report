# Generazione automatica di un Report PDF con Python

## Descrizione del progetto

Questo progetto consiste nella realizzazione di uno script Python in grado di generare automaticamente un **report in formato PDF** partendo da dati contenuti in due diversi formati:

* **JSON**
* **CSV**

Lo script legge i dati dai due file, li elabora e genera **due grafici** tramite la libreria Matplotlib. Successivamente utilizza la libreria ReportLab per creare un documento PDF contenente il titolo, la data di generazione, i grafici e una tabella con i dati provenienti dal file JSON.

---

## Obiettivi

Gli obiettivi principali del progetto sono:

* leggere e interpretare un file JSON;
* leggere e interpretare un file CSV;
* estrarre i dati necessari;
* utilizzare le **list comprehension** di Python;
* generare grafici con Matplotlib;
* creare un documento PDF con ReportLab;
* inserire immagini e tabelle nel PDF;
* aggiungere automaticamente la data e l'ora di generazione del report;
* ottenere un report finale generato automaticamente.

---

## Tecnologie utilizzate

Il progetto è stato realizzato utilizzando:

* **Python**
* **JSON**
* **CSV**
* **Matplotlib**
* **ReportLab**

### Librerie Python

Le librerie principali utilizzate sono:

```python
import json
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
```

Per la generazione del PDF vengono utilizzati diversi componenti di ReportLab:

```python
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
```

---

## Struttura del progetto

La struttura dei file utilizzata è:

```text
report_python/
│
├── genera_report.py
├── dati.json
├── dati.csv
├── grafico.png
├── grafico_vendite.png
└── report.pdf
```

### File di input

* `dati.json` → contiene i dati utilizzati per il primo grafico e per la tabella.
* `dati.csv` → contiene i dati relativi alle vendite mensili utilizzati per il secondo grafico.

### File generati

* `grafico.png` → grafico generato a partire dai dati JSON.
* `grafico_vendite.png` → grafico a barre generato a partire dai dati CSV.
* `report.pdf` → documento finale generato dal programma.

---

# 1. File JSON

Il file `dati.json` contiene un titolo e una lista di dati organizzati attraverso le chiavi `x` e `y`.

Esempio:

```json
{
    "titolo": "Report vendite",
    "dati": [
        {
            "x": "Gennaio",
            "y": 120
        },
        {
            "x": "Febbraio",
            "y": 150
        },
        {
            "x": "Marzo",
            "y": 180
        },
        {
            "x": "Aprile",
            "y": 160
        },
        {
            "x": "Maggio",
            "y": 210
        }
    ]
}
```

Il programma apre il file:

```python
with open("dati.json", "r", encoding="utf-8") as file:
    dati_json = json.load(file)
```

La funzione `json.load()` converte il contenuto del file JSON in un **oggetto Python**, in questo caso un dizionario.

Successivamente vengono estratti:

```python
titolo = dati_json["titolo"]
dati = dati_json["dati"]
```

La variabile `titolo` contiene il titolo del report, mentre `dati` contiene la lista dei dati.

---

# 2. File CSV

Il file `dati.csv` contiene i dati relativi alle vendite mensili.

Esempio:

```csv
mese,vendite
Gennaio,120
Febbraio,150
Marzo,180
Aprile,160
Maggio,210
```

Il programma utilizza `csv.DictReader` per leggere il file:

```python
with open("dati.csv", "r", encoding="utf-8") as file:
    lettore = csv.DictReader(file)

    for riga in lettore:
        mesi.append(riga["mese"])
        vendite.append(int(riga["vendite"]))
```

Vengono create due liste:

```python
mesi = []
vendite = []
```

La lista `mesi` contiene i mesi, mentre la lista `vendite` contiene i relativi valori numerici.

Il valore delle vendite viene convertito da stringa a intero attraverso:

```python
int(riga["vendite"])
```

---

# 3. Creazione del grafico CSV

I dati provenienti dal CSV vengono utilizzati per creare un **grafico a barre**.

Per prima cosa viene creata una nuova figura:

```python
plt.figure(figsize=(8, 5))
```

Successivamente viene utilizzata:

```python
plt.bar(
    mesi,
    vendite
)
```

La funzione `plt.bar()` crea un diagramma a barre verticali.

Vengono poi aggiunti:

```python
plt.title("Vendite mensili")
plt.xlabel("Mese")
plt.ylabel("Vendite")
```

Questi comandi impostano:

* titolo del grafico;
* etichetta dell'asse X;
* etichetta dell'asse Y.

Infine il grafico viene salvato:

```python
grafico_csv = "grafico_vendite.png"

plt.savefig(
    grafico_csv,
    dpi=150
)
```

Il risultato è il file:

```text
grafico_vendite.png
```

---

# 4. Estrazione dei dati X e Y dal JSON

I dati presenti nel JSON vengono utilizzati per creare due liste separate:

```python
x = [elemento["x"] for elemento in dati]     
y = [elemento["y"] for elemento in dati]     
```           
Questa tecnica viene chiamata **list comprehension**.                               

Può anche essere scritta in questo modo in maniera piu esplicita -->
--------------------------------------------------
x = []
y = []

for elemento in dati:
    x.append(elemento["x"])
    y.append(elemento["y"])
---------------------------------------------------


Python scorre ogni elemento presente nella lista `dati` e recupera:

* il valore della chiave `x` → lista `x`;
* il valore della chiave `y` → lista `y`.

Ad esempio:

```text
x = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio"]

y = [120, 150, 180, 160, 210]
```

Queste liste vengono successivamente utilizzate per creare il grafico.

---

# 5. Creazione del grafico JSON

Per i dati JSON viene creato un **grafico a linee**:

```python
plt.figure(figsize=(10, 5))

plt.plot(
    x,
    y,
    marker="o"
)
```

La funzione `plt.plot()` utilizza le liste `x` e `y` come coordinate del grafico.

L'opzione:

```python
marker="o"
```

permette di visualizzare un punto in corrispondenza dei valori.

Vengono inoltre aggiunti:

```python
plt.title(titolo)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
```

Il grafico viene quindi salvato nel file:

```text
grafico.png
```

---

# 6. Creazione del PDF

Il documento PDF viene creato utilizzando ReportLab.

Il percorso del file viene definito con:

```python
pdf_path = "report.pdf"
```

Successivamente viene creato il documento: -->(viene creato un oggetto Python grazie alla classe SimpleDocTemplate che crea appunto un pdf)

```python
documento = SimpleDocTemplate(
    pdf_path,
    pagesize=A4
)
```

Il formato della pagina viene impostato su **A4**.

---

# 7. Preparazione del contenuto

Per gestire gli stili del documento viene utilizzato:

```python
styles = getSampleStyleSheet()
```

Viene inoltre creata una lista vuota:

```python
contenuto = []
```

Questa lista contiene tutti gli elementi che verranno inseriti nel PDF.

---

# 8. Inserimento del titolo

Il titolo proveniente dal file JSON viene inserito nel PDF:

```python
contenuto.append(
    Paragraph(
        titolo,
        styles["Title"]
    )
)
```

In questo modo il PDF utilizza automaticamente il valore presente nella chiave `titolo` del JSON.

---

# 9. Inserimento della data di generazione

Il programma recupera automaticamente la data e l'ora correnti:

```python
data_generazione = datetime.now().strftime(
    "%d/%m/%Y %H:%M"
)
```

La data viene successivamente inserita nel documento:

```python
contenuto.append(
    Paragraph(
        f"Report generato il: {data_generazione}",
        styles["Normal"]
    )
)
```

In questo modo ogni report mostra il momento in cui è stato generato.

---

# 10. Inserimento del grafico JSON nel PDF

Il grafico creato da Matplotlib viene caricato come immagine:

```python
immagine = Image(
    grafico_path,
    width=500,
    height=250
)
```

L'immagine viene poi aggiunta al contenuto del PDF:

```python
contenuto.append(immagine)
```

---

# 11. Inserimento del grafico CSV nel PDF

Anche il grafico delle vendite mensili viene inserito nel documento:

```python
immagine_csv = Image(
    grafico_csv,
    width=500,
    height=250
)

contenuto.append(immagine_csv)
```

Il PDF contiene quindi **due grafici**:

1. grafico dei dati JSON;
2. grafico delle vendite mensili provenienti dal CSV.

---

# 12. Creazione della tabella JSON

Il programma crea una tabella utilizzando i dati presenti nel JSON.

La prima riga contiene le intestazioni:

```python
tabella_dati = [["X", "Y"]]
```

Successivamente viene utilizzato un ciclo `for`:

```python
for elemento in dati:
    tabella_dati.append([
        elemento["x"],
        elemento["y"]
    ])
```

In questo modo vengono aggiunti alla tabella tutti i valori `x` e `y`.

---

# 13. Formattazione della tabella

La tabella viene creata con:

```python
tabella = Table(tabella_dati)
```

Successivamente viene applicato uno stile:

```python
tabella.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("PADDING", (0, 0), (-1, -1), 6)
    ])
)
```

La formattazione permette di:

* colorare lo sfondo dell'intestazione;
* impostare il colore del testo dell'intestazione;
* creare i bordi della tabella;
* centrare il contenuto;
* aggiungere spazio interno alle celle.

---

# 14. Generazione del PDF

Dopo aver inserito tutti gli elementi, il documento viene generato con:

```python
documento.build(contenuto)
```

Il file finale viene salvato come:

```text
report.pdf
```

Infine il programma mostra nel terminale:

```python
print(f"Report creato: {pdf_path}")
```

---

# Flusso completo del progetto

Il funzionamento generale può essere rappresentato nel seguente modo:

```text
                  DATI
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
      dati.json          dati.csv
          │                 │
          ▼                 ▼
    Lettura JSON       Lettura CSV
          │                 │
          ▼                 ▼
      Dati X/Y       Mesi e vendite
          │                 │
          ▼                 ▼
      Grafico a          Grafico a
        linee              barre
          │                 │
          └────────┬────────┘
                   ▼
              ReportLab
                   │
          ┌────────┼────────┐
          │        │        │
          ▼        ▼        ▼
       Titolo   Grafici   Tabella
          │        │        │
          └────────┼────────┘
                   ▼
              report.pdf
```

---

# Installazione

Per eseguire il progetto è necessario avere Python installato.

Dal terminale, nella cartella del progetto, installare le librerie necessarie:

```bash
pip install matplotlib reportlab
```

I moduli `json`, `csv`, `os` e `datetime` fanno parte della libreria standard di Python e non richiedono installazioni aggiuntive.

---

# Esecuzione

Per eseguire il programma:

```bash
python genera_report.py
```

Se l'esecuzione termina correttamente, nel terminale verrà visualizzato:

```text
Report creato: report.pdf
```

Nella cartella del progetto saranno presenti il PDF e i grafici generati.

---

# Output finale

Il programma produce:

```text
grafico.png
```

Grafico a linee creato utilizzando i dati del JSON.

```text
grafico_vendite.png
```

Grafico a barre creato utilizzando i dati del CSV.

```text
report.pdf
```

Report finale contenente:

* titolo;
* data e ora di generazione;
* grafico dei dati JSON;
* grafico delle vendite CSV;
* tabella dei dati JSON.

---

# Conclusione

Il progetto dimostra come Python possa essere utilizzato per **leggere, elaborare e rappresentare dati provenienti da formati differenti**, come JSON e CSV.

I dati vengono trasformati in grafici tramite **Matplotlib** e successivamente raccolti all'interno di un unico documento PDF tramite **ReportLab**.

Il risultato è un processo automatizzato che permette di passare dai dati di input al report finale attraverso un unico script Python.

---
