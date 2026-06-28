import collections

_history = collections.deque(maxlen=60)


def add(pressure):
    if pressure is not None:
        _history.append(pressure)


def slope():
    n = len(_history)

    if n < 10:
        return None

    xs = list(range(n))
    ys = list(_history)

    mx = sum(xs) / n
    my = sum(ys) / n

    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))

    return num / den if den else 0.0


def label():
    s = slope()

    if s is None:
        return "collecting"

    if s > 0.05:
        return "clear"

    if s < -0.05:
        return "rain"

    return "stable"


def text():
    l = label()

    if l == "collecting":
        return "Collecting data..."

    if l == "clear":
        return "?? Clear weather coming"

    if l == "rain":
        return "??? Rain likely"

    return "??? Stable conditions"