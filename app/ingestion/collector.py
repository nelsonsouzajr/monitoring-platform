import requests
import time
from datetime import datetime
import os

from app.normalization.schemas import APIMetric

SIMULATOR_URL = os.getenv("SIMULATOR_URL")


def collect_metric() -> APIMetric:
    endpoint = "/metrics"
    url = f"{SIMULATOR_URL}{endpoint}"

    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        success = response.status_code < 500
    except requests.RequestException:
        status_code = 500
        success = False
    end = time.perf_counter()

    response_time_ms = (end - start) * 1000

    # Tenta obter o modo atual
    try:
        health = requests.get(f"{SIMULATOR_URL}/health", timeout=2).json()
        mode = health.get("mode", "unknown")
    except requests.RequestException:
        mode = "unknown"

    return APIMetric(
        timestamp=datetime.utcnow(),
        source="api_simulator",
        endpoint=endpoint,
        method="GET",
        response_time_ms=response_time_ms,
        status_code=status_code,
        success=success,
        mode=mode
    )
