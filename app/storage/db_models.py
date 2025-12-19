from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from app.storage.database import Base  

class ApiMetric(Base):
    __tablename__ = "api_metrics"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    source = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)
    response_time_ms = Column(Float, nullable=False)
    status_code = Column(Integer, nullable=False)
    success = Column(Boolean, nullable=False)
    mode = Column(String, nullable=False)
