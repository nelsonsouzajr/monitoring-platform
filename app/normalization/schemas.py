from pydantic import BaseModel
from datetime import datetime


class APIMetric(BaseModel):
    timestamp: datetime
    source: str
    endpoint: str
    method: str
    response_time_ms: float
    status_code: int
    success: bool
    mode: str
