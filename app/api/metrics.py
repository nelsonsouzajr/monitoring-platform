from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.storage.database import SessionLocal
from app.storage.repository import (
    get_metrics,
    get_metrics_summary,
    get_latency_percentiles,
)

router = APIRouter(prefix="/metrics", tags=["metrics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_metrics(limit: int = 100, db: Session = Depends(get_db)):
    return get_metrics(db, limit)


@router.get("/summary")
def metrics_summary():
    data = get_metrics_summary()

    return {
        "avg_response_ms": data.avg_response,
        "p95_response_ms": data.p95_response,
        "success_rate": (
            data.success_count / data.total_count
            if data.total_count else 0
        ),
        "anomaly_count": data.anomaly_count,
        "total_requests": data.total_count,
    }


@router.get("/anomalies")
def anomalies(limit: int = 50):
    return get_anomalies(limit)


@router.get("/latency")
def latency_percentiles(db: Session = Depends(get_db)):
    p95, p99 = get_latency_percentiles(db)
    return {"p95": p95, "p99": p99}
