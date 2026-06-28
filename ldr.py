from gpiozero import DigitalInputDevice

_sensor = None


def ldr(pin):
    global _sensor
    _sensor = DigitalInputDevice(pin)


def value():
    if _sensor is None:
        return None
    return _sensor.value


def is_light():
    if _sensor is None:
        return None
    return bool(_sensor.value)


def is_dark():
    if _sensor is None:
        return None
    return not bool(_sensor.value)