from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Nitya Jhaveri Portfolio API")

# Allow frontend to call the API from any origin in this dev environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Portfolio backend is running"}


@app.get("/health")
def health():
    return {"ok": True}
