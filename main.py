from fastapi import FastAPI 

app = FastAPI(title="Filing Extraction API")

@app.get("/")
def root():
    return {"message": "Filing Extraction API"}

@app.get("/health")
def health():
    return {"status": "ok"}