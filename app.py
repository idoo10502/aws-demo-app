from fastapi import FastAPI
import socket
import datetime
import uuid

app = FastAPI()

VERSION = "v2"


@app.get("/")
def root():
    return {"status": "ok", "message": "demo-app is running"}


@app.get("/info")
def info():
    """No database, no shared storage — every response is computed fresh from
    whatever process happens to handle this specific request."""
    return {
        "version": VERSION,
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "request_id": str(uuid.uuid4()),
        "message": "This is a stateless service — nothing is remembered between requests",
    }
