from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Health Check
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

# Input schema
class MatchRequest(BaseModel):
    resume: str
    jobs: List[str]

# Resume matching logic
def match_resume_to_jobs(resume: str, job_descriptions: List[str]):
    texts = [resume] + job_descriptions
    vectorizer = TfidfVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    scores = cosine_similarity([vectors[0]], vectors[1:])[0]
    return [{"job": job, "score": float(score)} for job, score in zip(job_descriptions, scores)]

# Match endpoint
@app.post("/match")
def match_endpoint(data: MatchRequest):
    scores = match_resume_to_jobs(data.resume, data.jobs)
    return {"matches": scores}
