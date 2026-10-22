from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ALFRED — vitrine")
app.include_router(router, prefix="/api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
