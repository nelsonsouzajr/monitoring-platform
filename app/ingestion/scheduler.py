import time
import os
from datetime import datetime

from app.analytics.anomaly import detect_anomaly
from app.storage.repository import (
    save_metric,
    get_recent_response_times
)
from app.storage.db_models import ApiMetric
from app.ingestion.collector import collect_metric

INTERVAL = int(os.getenv("INGESTION_INTERVAL_SECONDS", "30"))


def run():
    print("Ingestion worker started")

    while True:
        metric_data = collect_metric()

        history = get_recent_response_times(
            endpoint=metric_data["endpoint"]
        )

        status = detect_anomaly(
            values=history,
            current=metric_data["response_time_ms"]
        )

        metric = ApiMetric(
            timestamp=datetime.utcnow(),
            source="api_simulator",
            endpoint=metric_data["endpoint"],
            method=metric_data["method"],
            response_time_ms=metric_data["response_time_ms"],
            status_code=metric_data["status_code"],
            success=metric_data["success"],
            mode=status
        )

        save_metric(metric)

        time.sleep(INTERVAL)
