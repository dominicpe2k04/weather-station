import board
import adafruit_dht

_sensor = None


def dht(pin):
    global _sensor
    board_pin = getattr(board, f"D{pin}")
    _sensor = adafruit_dht.DHT11(board_pin)


def temperature():
    try:
        return _sensor.temperature
    except RuntimeError:
        return None


def humidity():
    try:
        return _sensor.humidity
    except RuntimeError:
        return None