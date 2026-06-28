from flask import Flask, jsonify, render_template

import dht11
import ldr
import bmp180
import predictor

app = Flask(__name__)

dht11.dht(4)
ldr.ldr(17)
bmp180.bmp180()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/data")
def data():
    pressure = bmp180.pressure()

    predictor.add(pressure)

    return jsonify({
        "temperature": dht11.temperature(),
        "humidity": dht11.humidity(),
        "pressure": pressure,
        "light": ldr.value(),
        "prediction": predictor.label(),
        "prediction_text": predictor.text()
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )