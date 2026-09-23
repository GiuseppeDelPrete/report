# Generatore di Report per Misurazioni Sensori

Applicazione Python per l'elaborazione di misurazioni provenienti da sensori e la generazione automatica di report in formato PDF, corredati da grafici e tabelle.

Il progetto è stato sviluppato utilizzando **Python**, **Matplotlib** e **ReportLab**, con gestione del codice tramite **Git e GitHub**.

## Descrizione

Il progetto permette di elaborare le misurazioni provenienti da un numero variabile di sensori e di generare automaticamente un report in formato PDF.

Il programma legge i dati dal file:

```text
sensor_measurements.json
```

e utilizza le informazioni contenute nel file per:

1. leggere il parametro misurato;
2. leggere l'unità di misura;
3. leggere l'intervallo di campionamento;
4. leggere le misurazioni dei due sensori;
5. filtrare le misurazioni in base al periodo selezionato;
6. generare un grafico dell'andamento dei sensori;
7. creare un report PDF;
8. inserire nel PDF il grafico e una tabella delle misurazioni.

---

## Funzionalità

### Lettura del file JSON

Il programma utilizza il file:

```text
sensor_measurements.json
```

per recuperare i dati relativi alle misurazioni dei sensori.

Il file contiene informazioni sul parametro misurato, sull'unità di misura, sull'intervallo di campionamento e sui valori rilevati dai sensori.

### Generazione del grafico

Il programma utilizza la libreria **Matplotlib** per generare un grafico, nel caso in esame, contenente l'andamento delle misurazioni di:

* Sensor 1
* Sensor 2
* Sensor 3

Il grafico viene salvato nel file:

```text
grafico.png
```

### Generazione del report PDF

Il programma utilizza la libreria **ReportLab** per generare automaticamente il report.

Il PDF contiene:

* titolo del report;
* data e ora di generazione;
* periodo selezionato;
* intervallo di campionamento;
* grafico delle misurazioni;
* tabella con i dati dei sensori.

### Selezione del periodo

È possibile scegliere il periodo delle misurazioni utilizzando i parametri:

```text
--data-inizio
--data-fine
```

Il programma utilizza queste date per selezionare le misurazioni comprese nel periodo indicato.

### Nome del file di output

È possibile specificare il nome del file PDF generato utilizzando:

```text
--output
```

---

## Struttura del progetto

La struttura principale del progetto è la seguente:

```text
report/
│
├── genera_report.py
├── sensor_measurements.json
├── README.md
├── requirements.txt
```

### Descrizione dei file

| File                       | Descrizione                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| `genera_report.py`         | Script principale che legge i dati, filtra le misurazioni, genera il grafico e crea il PDF |
| `sensor_measurements.json` | File JSON contenente le misurazioni dei sensori                                            |
| `requirements.txt`         | Elenco delle librerie Python necessarie                                                    |
| `README.md`                | Documentazione del progetto                                                                |

---

## Requisiti

Per eseguire il progetto è necessario avere installato:

* **Python 3**
* **Matplotlib**
* **ReportLab**
* **Git** per la gestione del repository

---

## Installazione

### 1. Verificare l'installazione di Python

Aprire il terminale di Visual Studio Code e verificare che Python sia installato:

```powershell
python --version
```

Dovrebbe essere visualizzata la versione di Python installata.

---

### 2. Installare le librerie necessarie

Installare Matplotlib e ReportLab utilizzando `pip`:

```powershell
pip install matplotlib reportlab
```

È possibile verificare l'installazione con:

```powershell
pip show matplotlib
```

e:

```powershell
pip show reportlab
```

---

## Utilizzo

Per eseguire il programma bisogna aprire il terminale di Visual Studio Code nella cartella del progetto.

### Esecuzione senza parametri

Il programma può essere eseguito semplicemente con:

```powershell
python genera_report.py
```

In questo caso verrà utilizzato il file:

```text
sensor_measurements.json
```

e il report verrà generato con il nome predefinito:

```text
report.pdf
```

---

### Esecuzione con selezione del periodo

È possibile specificare una data iniziale e una data finale.

Esempio:

```powershell
python genera_report.py --data-inizio 2026-09-01 --data-fine 2026-09-18
```

Il programma considererà solamente le misurazioni comprese nel periodo indicato.

---

### Esecuzione con nome personalizzato del PDF

È possibile scegliere il nome del file PDF utilizzando `--output`.

Esempio:

```powershell
python genera_report.py --output report_settembre.pdf
```

In questo caso il report verrà salvato come:

```text
report_settembre.pdf
```

---

### Esecuzione completa

È possibile utilizzare contemporaneamente tutti i parametri:

```powershell
python genera_report.py --data-inizio 2026-09-01 --data-fine 2026-09-18 --output report_settembre.pdf
```

In questo esempio:

* la data iniziale è `2026-09-01`;
* la data finale è `2026-09-18`;
* il file PDF viene salvato come `report_settembre.pdf`.

---

## Parametri da riga di comando

Lo script supporta i seguenti parametri:

| Parametro       | Descrizione                              | Esempio                    |
| --------------- | ---------------------------------------- | -------------------------- |
| `--data-inizio` | Data iniziale del periodo da considerare | `--data-inizio 2026-09-01` |
| `--data-fine`   | Data finale del periodo da considerare   | `--data-fine 2026-09-18`   |
| `--output`      | Nome del file PDF da generare            | `--output report.pdf`      |

### Formato delle date

Le date devono essere inserite nel formato:

```text
YYYY-MM-DD
```

Ad esempio:

```text
2026-09-01
```

Il programma controlla inoltre che la data iniziale non sia successiva alla data finale.

---

## File JSON

Il file `sensor_measurements.json` contiene i dati utilizzati dallo script.

La struttura del file è basata sulle seguenti informazioni:

```json
{
    "parameter": "temperature",
    "unit": "°C",
    "sampling_interval_minutes": 10,
    "measurements": [
        {
            "timestamp": "2026-09-01T10:00:00Z",
            "sensor_1": 24.5,
            "sensor_2": 25.1
        }
    ]
}
```

### Campi principali

| Campo                       | Descrizione                                    |
| --------------------------- | ---------------------------------------------- |
| `parameter`                 | Indica il parametro misurato                   |
| `unit`                      | Indica l'unità di misura                       |
| `sampling_interval_minutes` | Indica l'intervallo di campionamento in minuti |
| `measurements`              | Contiene l'elenco delle misurazioni            |

Ogni elemento della lista `measurements` contiene:

| Campo       | Descrizione                         |
| ----------- | ----------------------------------- |
| `timestamp` | Data e ora della misurazione        |
| `sensor_1`  | Valore rilevato dal primo sensore   |
| `sensor_2`  | Valore rilevato dal secondo sensore |

---

## Output

L'esecuzione dello script produce diversi risultati.

### Grafico

Il grafico viene salvato nel file:

```text
grafico.png
```

Il grafico rappresenta l'andamento dei valori rilevati da Sensor 1 e Sensor 2 nel periodo selezionato.

### Report PDF

Il report viene salvato nel file specificato tramite il parametro `--output`.

Se non viene specificato alcun nome, viene utilizzato:

```text
report.pdf
```

Il PDF contiene il grafico e una tabella con le misurazioni relative al periodo selezionato.

---

## Branch Git

Per lo sviluppo del progetto sono stati utilizzati quattro branch separati, in modo da sviluppare le funzionalità richieste separatamente.

### Branch `feature/json-input`

Questo branch è stato utilizzato per la funzionalità relativa al nuovo file JSON.

Il programma è stato modificato per utilizzare:

```text
sensor_measurements.json
```

come file contenente le misurazioni dei sensori.

---

### Branch `feature/parameters-config`

Questo branch è stato utilizzato per aggiungere la gestione dei parametri da riga di comando.

Sono stati aggiunti:

```text
--data-inizio
--data-fine
--output
```

Questi parametri permettono di:

* selezionare il periodo delle misurazioni;
* scegliere il nome del file PDF generato.

### Branch 'feature/input-parameter'

#### Specificare il file di input

Il programma permette di specificare tramite riga di comando il file JSON contenente le misurazioni da elaborare.

Per indicare un file JSON diverso da quello utilizzato come valore predefinito, è possibile utilizzare il parametro:

```bash
--input
```
Per ottenere questo comportamento si aggiunge questo pezzo di codice:

```python
parser.add_argument(
    "--input",
    type=str,
    default="sensor_measurements.json",
    help="Nome del file JSON di input"
)
```
E poi sostituire il nome del file predefinito, che era sensor_measurements.json, con args.input

```python
with open(
    args.input,
    "r",
    encoding="utf-8"
) as file:
    dati_json = json.load(file)
```

Ad esempio:

```bash
python genera_report.py --input dati.json
```

È possibile utilizzare il parametro `--input` insieme agli altri parametri disponibili, come `--output`, `--data-inizio` e `--data-fine`.

Esempio:

```bash
python genera_report.py --input misurazioni.json --output report.pdf --data-inizio 2026-01-01 --data-fine 2026-06-30
```

In questo modo il programma legge i dati dal file JSON specificato dall'utente, applica eventualmente il filtro relativo al periodo indicato e genera il report PDF con il nome scelto.

Il parametro `--input` rende quindi il programma più flessibile, perché non è più necessario utilizzare sempre lo stesso file JSON presente nella cartella del progetto.

### Branch - multi-sensori-grafici 
Obiettivi del branch

1. Supporto a più di due sensori
***Permettere al programma di acquisire e gestire le misurazioni di un numero variabile di sensori***

2. Grafici individuali e confronto finale
***Generare un grafico per ogni sensore e mantenere il grafico di confronto già esistente alla fine del report***

--- 

## Rilevamento dei sensori

I sensori vengono individuati automaticamente analizzando le chiavi presenti nella prima misurazione.

```python
timestamps = [
    mis["timestamp"]
    for mis in misurazioni_filtrate
]

sensori = sorted(
    key
    for key in misurazioni_filtrate[0]
    if key.startswith("sensor_")
)
```

Il programma considera come sensori tutte le chiavi che iniziano con `sensor_`.
In questo modo non è necessario specificare manualmente nel codice quali sensori utilizzare.
Ad esempio, aggiungendo `sensor_3` ai dati, il programma lo rileva automaticamente.

---

## Creazione dei grafici singoli

Per ogni sensore rilevato viene creato automaticamente un grafico individuale.

Il programma utilizza un ciclo `for` per evitare di dover scrivere manualmente il codice per ogni sensore.

```
for sensore in sensori:
    valori = [
        mis[sensore]
        for mis in misurazioni_filtrate
    ]
    ...
```

Per ogni sensore viene generato un file PNG separato:
```
grafico_sensor_1.png
grafico_sensor_2.png
grafico_sensor_3.png
```

Il numero di grafici generati dipende quindi dal numero di sensori presenti nei dati.

---

## Grafico di confronto

Oltre ai grafici individuali, il programma genera un grafico contenente tutti i sensori.

```
plt.figure(
    figsize=(10, 5)
)
for sensore in sensori:
    valori = [
        mis[sensore]
        for mis in misurazioni_filtrate
    ]
    plt.plot(
        timestamps,
        valori,
        marker="o",
        label=sensore
    )
```

Ogni sensore viene aggiunto al grafico tramite il ciclo `for`.

Il risultato viene salvato nel file:
`grafico_confronto.png`

In questo modo è possibile confrontare l'andamento di tutti i sensori all'interno dello stesso grafico.

---

## Inserimento dei grafici nel PDF

I grafici individuali vengono inseriti automaticamente nel documento PDF utilizzando la lista `grafici_singoli`.

I nomi dei sensori e i relativi file grafici vengono associati tramite `zip()`:

`for sensore, grafico_path in zip(sensori, grafici_singoli):    ...`

In questo modo il PDF può contenere un numero variabile di grafici, in base al numero di sensori rilevati.

Ogni grafico viene inserito con il nome del sensore come titolo.

Anche il grafico di confronto viene inserito automaticamente nel PDF utilizzando il percorso contenuto nella variabile `grafico_confronto_path`.

---

## Tabella dinamica

Anche la tabella del PDF è stata resa dinamica.
L'intestazione viene costruita utilizzando direttamente la lista dei sensori:
```
tabella_dati = [
    [
        "Timestamp",
        *sensori
    ]
]
```
Successivamente, per ogni misurazione, viene creata una riga contenente il timestamp e i valori di tutti i sensori:
```
for mis in misurazioni_filtrate:
    riga = [
        mis["timestamp"]
    ]
    for sensore in sensori:
        riga.append(
            str(mis[sensore])
        )
    tabella_dati.append(
        riga
    )
```
In questo modo la tabella si adatta automaticamente al numero di sensori presenti nei dati.

Ad esempio, con tre sensori viene generata una tabella con:

`Timestamp | sensor_1 | sensor_2 | sensor_3 `

Non è necessario modificare manualmente il codice ogni volta che viene aggiunto un nuovo sensore

---

## Comandi Git utilizzati

### Inizializzazione del repository

```powershell
git init
```

### Verifica dello stato del repository

```powershell
git status
```

### Aggiunta dei file

Per aggiungere un file specifico:

```powershell
git add genera_report.py
```

Per aggiungere più file:

```powershell
git add grafico.png report.pdf
```

### Creazione del commit

```powershell
git commit -m "Messaggio del commit"
```

### Collegamento al repository GitHub

```powershell
git remote add origin https://github.com/GiuseppeDelPrete/report
```

### Verifica del repository remoto

```powershell
git remote -v
```

### Creazione del branch JSON

```powershell
git checkout -b feature/json-input
```

### Creazione del branch dei parametri

```powershell
git checkout -b feature/parameters-config
```

### Visualizzazione dei branch

```powershell
git branch
```

### Passaggio a un branch

Per passare al branch JSON:

```powershell
git checkout feature/json-input
```

Per passare al branch dei parametri:

```powershell
git checkout feature/parameters-config
```

### Caricamento delle modifiche su GitHub

```powershell
git push
```

Per il primo caricamento di un nuovo branch può essere utilizzato:

```powershell
git push -u origin feature/parameters-config
```

---

## Tecnologie utilizzate

Il progetto utilizza le seguenti tecnologie:

* **Python** — linguaggio di programmazione utilizzato per lo sviluppo dello script;
* **JSON** — formato utilizzato per memorizzare le misurazioni;
* **Matplotlib** — libreria utilizzata per la generazione dei grafici;
* **ReportLab** — libreria utilizzata per la generazione dei documenti PDF;
* **Git** — sistema di controllo versione;
* **GitHub** — piattaforma utilizzata per il repository remoto.

---