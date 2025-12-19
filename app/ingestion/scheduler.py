import time
import os

from app.ingestion.collector import collect_metric
from app.storage.repository import save_metric

INTERVAL = int(os.getenv("INGESTION_INTERVAL_SECONDS", "30"))

def run():
    print("Ingestion worker started")
    while True:
        metric = collect_metric()
        save_metric(metric)
        print(f"Metric collected: {metric}")
        time.sleep(INTERVAL)
