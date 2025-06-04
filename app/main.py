from fastapi import FastAPI, Request
from pydantic import BaseModel
from matcher import match_resume_to_jobs

app = FastAPI()

class MatchRequest(BaseModel):
    resume: str
    jobs: list[str]

@app.post("/match")
def match_endpoint(data: MatchRequest):
    scores = match_resume_to_jobs(data.resume, data.jobs)
    return {"matches": scores}
