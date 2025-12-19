import time
from fastapi import FastAPI
from app.api.router import router as api_router
from sqlalchemy.exc import OperationalError
import app.storage.db_models
from app.ingestion.scheduler import run
from app.storage.database import engine, Base

app = FastAPI(title="Monitoring Platform")

def init_db_with_retry(retries: int = 10, delay: int = 3):
    for attempt in range(1, retries + 1):
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected successfully")
            return
        except OperationalError:
            print(
                f"DB not ready (attempt {attempt}/{retries}), retrying in {delay}s..."
            )
            time.sleep(delay)

    raise RuntimeError("Database not available after retries")


if __name__ == "__main__":
    app.include_router(api_router)
    init_db_with_retry()
    run()
