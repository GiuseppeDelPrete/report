# Generatore di Report per Misurazioni Sensori

Applicazione Python per l'elaborazione di misurazioni provenienti da sensori e la generazione automatica di report in formato PDF, corredati da grafici e tabelle.

Il progetto è stato sviluppato utilizzando **Python**, **Flask**, **Matplotlib** e **ReportLab**, con gestione del codice tramite **Git e GitHub**.

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
4. leggere le misurazioni dei sensori;
5. filtrare le misurazioni in base al periodo selezionato;
6. generare grafici individuali e un grafico comparativo dell'andamento dei sensori;
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

### Generazione dei grafici

Il programma utilizza la libreria **Matplotlib** per rilevare automaticamente i sensori presenti nel file JSON e generare i relativi grafici.

Per ogni sensore viene generato un grafico individuale contenente l'andamento delle misurazioni nel tempo.

Ad esempio, per tre sensori vengono creati:

```text
grafico_sensor_1.png
grafico_sensor_2.png
grafico_sensor_3.png
```

Il programma genera inoltre un grafico comparativo contenente l'andamento di tutti i sensori:

```text
grafico_confronto.png
```

In questo modo il programma può gestire automaticamente un numero variabile di sensori senza dover modificare il codice.

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
├── app.py
├── sensor_measurements.json
├── Dockerfile
├── README.md
└── requirements.txt

### Descrizione dei file

| File                        | Descrizione                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| `genera_report.py`          | Script principale che legge i dati, filtra le misurazioni, genera i grafici e crea il PDF |
| `sensor_measurements.json`  | File JSON contenente le misurazioni dei sensori                                            |
| `requirements.txt`          | Elenco delle librerie Python necessarie                                                    |
| `README.md`                 | Documentazione del progetto                                                                |
| `app.py`                    | Applicazione Flask che espone l'endpoint API per la generazione del report                |
| `Dockerfile`                | File contenente le istruzioni per creare l'immagine Docker dell'applicazione              |
---

## Requisiti

Per eseguire il progetto è necessario avere installato:

* **Python 3**
* **Matplotlib**
* **ReportLab**
* **Git** per la gestione del repository
* **Flask** per la realizzazione dell'API
* **Docker Desktop** se si desidera eseguire il progetto tramite Docker

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

Installare Matplotlib, Flask e ReportLab utilizzando `pip`:

```powershell
pip install flask matplotlib reportlab
```

È possibile verificare l'installazione con:

```powershell
pip show matplotlib
```

e:

```powershell
pip show reportlab
```
e:

```powershell
pip show flask
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
| `--input`       | Nome del file JSON di input              | `--input sensor_measurements.json` |

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
            "sensor_1": 22.0,
            "sensor_2": 21.1,
            "sensor_3": 25.1
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
| `sensor_3`  | Valore rilevato dal terzo sensore   |

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

Per lo sviluppo del progetto sono stati utilizzati cinque branch separati, in modo da sviluppare le funzionalità richieste separatamente.

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


### Branch - feature/api-endpoint

## API Flask

Il progetto dispone anche di un'API realizzata utilizzando **Flask**.

L'API permette di avviare la generazione del report tramite una richiesta HTTP, senza utilizzare direttamente la riga di comando.

L'applicazione Flask non dispone di un'interfaccia grafica. L'endpoint viene testato tramite **Postman**.

### Avvio dell'API

Per avviare il server Flask bisogna aprire il terminale di Visual Studio Code nella cartella del progetto ed eseguire:

```powershell
python app.py
```

Il server viene avviato all'indirizzo:

```text
http://127.0.0.1:5000
```

### Endpoint per la generazione del report

L'API espone il seguente endpoint:

```text
POST /genera-report
```

L'URL completo da utilizzare in Postman è:

```text
http://127.0.0.1:5000/genera-report
```

L'endpoint utilizza il metodo HTTP `POST` perché deve ricevere i parametri necessari alla generazione del report.

### Parametri dell'endpoint

I parametri vengono inviati nel **Body** della richiesta in formato JSON.

Esempio:

```json
{
    "input": "sensor_measurements.json",
    "output": "report.pdf",
    "data_inizio": "2026-09-18",
    "data_fine": "2026-09-18"
}
```

I parametri utilizzati sono:

| Parametro     | Descrizione                                  | Esempio                    |
| ------------- | -------------------------------------------- | -------------------------- |
| `input`       | Nome del file JSON contenente le misurazioni | `sensor_measurements.json` |
| `output`      | Nome del file PDF da generare                | `report.pdf`               |
| `data_inizio` | Data iniziale del periodo da considerare     | `2026-09-18`               |
| `data_fine`   | Data finale del periodo da considerare       | `2026-09-18`               |

I valori ricevuti dall'endpoint vengono passati alla funzione `genera_report()` presente nel file `genera_report.py`.

### Test tramite Postman

**### Test tramite Postman**

Per testare l'endpoint è possibile utilizzare Postman.

Configurare una nuova richiesta nel seguente modo:

**Metodo:**

```text
POST
```

**URL:**

```text
http://127.0.0.1:5000/genera-report
```

**Body:**

selezionare `raw` e successivamente `JSON`.

Inserire:

```json
{
    "input": "sensor_measurements.json",
    "output": "report.pdf",
    "data_inizio": "2026-09-18",
    "data_fine": "2026-09-18"
}
```

Premendo **Send**, Flask riceve la richiesta e avvia la funzione `genera_report()`.

Se la generazione termina correttamente, l'API restituisce direttamente il file PDF generato come risposta HTTP.

Il report è quindi disponibile nella risposta di Postman e può essere salvato o scaricato.

Il file PDF viene inoltre generato nella cartella del progetto con il nome specificato nel parametro `output`.

Ad esempio, utilizzando:

```json
"output": "report.pdf"
```

viene generato il file:

```text
report.pdf
```

**### Risposta dell'endpoint**

L'endpoint `/genera-report` restituisce il report PDF direttamente al client tramite la funzione Flask `send_file()`.

In questo modo il comportamento dell'API è il seguente:

```text
Postman
    ↓
HTTP POST + JSON
    ↓
Flask
    ↓
genera_report()
    ↓
generazione del PDF
    ↓
send_file()
    ↓
PDF restituito nella risposta HTTP
    ↓
Postman
```

Il client non riceve quindi solamente un messaggio di conferma in formato JSON, ma riceve direttamente il file PDF generato, pronto per essere salvato o scaricato.

### Separazione tra script e API

La funzione principale per la generazione del report è stata inserita nella funzione:

```python
genera_report(
    input_file,
    output_file,
    data_inizio_str,
    data_fine_str
)
```

In questo modo la stessa funzione può essere utilizzata sia dallo script eseguito tramite riga di comando sia dall'API Flask.

L'utilizzo di:

```python
if __name__ == "__main__":
```

permette di mantenere separata l'esecuzione tramite `argparse` dall'utilizzo della funzione da parte di `app.py`.

---

## Esecuzione con Docker

Il progetto può essere eseguito all'interno di un container Docker. Il `Dockerfile` contiene le istruzioni necessarie per creare l'immagine Docker con Python, le dipendenze e tutti i file del progetto.

### Modifica di `app.py`

Per permettere al server Flask di essere raggiungibile dall'esterno del container, è stato necessario modificare il metodo `app.run()` nel file `app.py`.

La configurazione utilizzata è:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

L'indirizzo `0.0.0.0` permette a Flask di ascoltare le connessioni su tutte le interfacce di rete del container. In questo modo Docker può inoltrare le richieste ricevute sulla porta `5000` del computer alla porta `5000` del container.

### Creazione dell'immagine Docker

Dalla cartella principale del progetto, dove si trova il file `Dockerfile`, eseguire:

```bash
docker build -t report-app .
```

Il comando crea un'immagine Docker chiamata `report-app`.

### Creazione e avvio del container

Dopo aver creato l'immagine, è possibile creare e avviare il container con:

```bash
docker run --name report-container -p 5000:5000 report-app
```

Il comando:

* `--name report-container` assegna il nome `report-container` al container;
* `-p 5000:5000` collega la porta 5000 del computer alla porta 5000 del container;
* `report-app` indica l'immagine Docker da utilizzare.

L'applicazione Flask viene avviata automaticamente dal container tramite il comando definito nel `Dockerfile`.

### Test dell'API

Una volta avviato il container, l'API è disponibile all'indirizzo:

```text
http://localhost:5000/genera-report
```

È possibile testare l'endpoint tramite Postman utilizzando una richiesta `POST` con il seguente JSON:

```json
{
    "input": "sensor_measurements.json",
    "output": "report.pdf",
    "data_inizio": "2026-09-18",
    "data_fine": "2026-09-18"
}
```

Il server Flask riceve i dati tramite l'API, genera il report PDF e lo restituisce al client tramite `send_file()`.


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
* **Flask** — framework utilizzato per realizzare l'API HTTP;
* **Postman** — strumento utilizzato per testare l'endpoint API.
* **Docker** - piattaforma che ha permesso la creazione ed eseguire l'applicazione all'interno del container

---