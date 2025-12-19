from fastapi import FastAPI, HTTPException
from modes import normal, slow, error, intermittent

app = FastAPI(title="API Service Simulator")

CURRENT_MODE = "normal"

MODE_MAP = {
    "normal": normal,
    "slow": slow,
    "error": error,
    "intermittent": intermittent
}

@app.get("/health")
def health():
    return {"status": "ok", "mode": CURRENT_MODE}

@app.post("/mode/{mode}")
def set_mode(mode: str):
    global CURRENT_MODE
    if mode not in MODE_MAP:
        raise HTTPException(status_code=400, detail="Invalid mode")
    CURRENT_MODE = mode
    return {"message": f"Mode set to {mode}"}

@app.get("/metrics")
def metrics():
    status_code = MODE_MAP[CURRENT_MODE]()
    if status_code >= 500:
        raise HTTPException(status_code=500, detail="Simulated error")
    return {"status": "success"}
