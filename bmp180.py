import random

_initialized = False


def bmp180():
    global _initialized
    _initialized = True


def temperature():
    if not _initialized:
        return None

    # Indoor temperature: 25-35�C
    return round(random.uniform(25.0, 35.0), 1)


def pressure():
    if not _initialized:
        return None

    # Typical atmospheric pressure: 980-1030 hPa
    return round(random.uniform(980.0, 1030.0), 1)


def altitude():
    if not _initialized:
        return None

    # Dummy altitude
    return round(random.uniform(0.0, 100.0), 1)