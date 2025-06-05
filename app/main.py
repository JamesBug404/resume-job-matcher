from fastapi import FastAPI, Request
from pydantic import BaseModel
from matcher import match_resume_to_jobs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
    
class MatchRequest(BaseModel):
    resume: str
    jobs: list[str]

@app.post("/match")
def match_endpoint(data: MatchRequest):
    scores = match_resume_to_jobs(data.resume, data.jobs)
    return {"matches": scores}
