from statistics import mean, stdev


def detect_anomaly(values: list[float], current: float) -> str:
    """
    Detecta anomalia baseada em Z-score.
    Retorna: normal | warning | anomaly
    """
    if len(values) < 5:
        return "normal"

    mu = mean(values)
    sigma = stdev(values)

    if sigma == 0:
        return "normal"

    z_score = (current - mu) / sigma

    if abs(z_score) >= 3:
        return "anomaly"
    elif abs(z_score) >= 2:
        return "warning"
    else:
        return "normal"
