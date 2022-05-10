import uvicorn
from fastapi import FastAPI

from router import router

app = FastAPI(
    title="Laboratorio de Programación - Trabajo Final (API server)",
    description="New York Times Top Stories",
    version="0.0.1",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
