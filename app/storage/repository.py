from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from app.storage.database import SessionLocal
from app.storage.db_models import ApiMetric


def save_metric(metric: ApiMetric):
    session: Session = SessionLocal()
    try:
        session.add(metric)
        session.commit()
    finally:
        session.close()
        

def get_metrics(db: Session, limit: int = 100):
    return (
        db.query(ApiMetric)
        .order_by(ApiMetric.timestamp.desc())
        .limit(limit)
        .all()
    )


def get_metrics_summary():
    session = SessionLocal()
    try:
        return session.query(
            func.avg(ApiMetric.response_time_ms).label("avg_response"),
            func.percentile_cont(0.95)
                .within_group(ApiMetric.response_time_ms)
                .label("p95_response"),
            func.sum(func.cast(ApiMetric.success, Integer)
                     ).label("success_count"),
            func.count(ApiMetric.id).label("total_count"),
            func.sum(
                func.case((ApiMetric.mode == "anomaly", 1), else_=0)
            ).label("anomaly_count"),
        ).one()
    finally:
        session.close()


def get_anomalies(limit: int = 50):
    session = SessionLocal()
    try:
        return (
            session.query(ApiMetric)
            .filter(ApiMetric.mode == "anomaly")
            .order_by(ApiMetric.timestamp.desc())
            .limit(limit)
            .all()
        )
    finally:
        session.close()


def get_latency_percentiles(db: Session):
    return db.execute(
        """
        SELECT
            percentile_cont(0.95) WITHIN GROUP (ORDER BY response_time_ms) AS p95,
            percentile_cont(0.99) WITHIN GROUP (ORDER BY response_time_ms) AS p99
        FROM api_metrics
        """
    ).one()
    

def get_recent_response_times(
    endpoint: str,
    window_minutes: int = 10,
    limit: int = 50
) -> list[float]:
    """
    Retorna os últimos tempos de resposta de um endpoint
    dentro de uma janela de tempo.
    """
    session: Session = SessionLocal()
    try:
        since = datetime.utcnow() - timedelta(minutes=window_minutes)

        results = (
            session.query(ApiMetric.response_time_ms)
            .filter(ApiMetric.endpoint == endpoint)
            .filter(ApiMetric.timestamp >= since)
            .order_by(ApiMetric.timestamp.desc())
            .limit(limit)
            .all()
        )

        return [row[0] for row in results]

    finally:
        session.close()
