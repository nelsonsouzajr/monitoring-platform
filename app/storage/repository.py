from sqlalchemy.orm import Session
from app.storage.database import SessionLocal
from sqlalchemy import func
from app.storage.db_models import ApiMetric


def save_metric(metric):
    session = SessionLocal()
    try:
        db_metric = ApiMetric(**metric.dict())
        session.add(db_metric)
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


def get_metrics_summary(db: Session):
    return db.query(
        func.count(ApiMetric.id).label("total"),
        func.avg(ApiMetric.response_time_ms).label("avg_latency"),
        func.min(ApiMetric.response_time_ms).label("min_latency"),
        func.max(ApiMetric.response_time_ms).label("max_latency"),
    ).one()


def get_latency_percentiles(db: Session):
    return db.execute(
        """
        SELECT
            percentile_cont(0.95) WITHIN GROUP (ORDER BY response_time_ms) AS p95,
            percentile_cont(0.99) WITHIN GROUP (ORDER BY response_time_ms) AS p99
        FROM api_metrics
        """
    ).one()
