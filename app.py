from flask import Flask, request, send_file
from genera_report import genera_report

app = Flask(__name__)


@app.route("/genera-report", methods=["POST"]) #creazione endpoint
def genera_report_endpoint():

    dati = request.get_json()

    input_file = dati.get("input", "sensor_measurements.json")
    output_file = dati.get("output", "report.pdf")
    data_inizio = dati.get("data_inizio")
    data_fine = dati.get("data_fine")

    genera_report(
        input_file,
        output_file,
        data_inizio,
        data_fine
    )

    return send_file(
        output_file,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)