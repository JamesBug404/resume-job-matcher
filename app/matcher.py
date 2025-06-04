from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_resume_to_jobs(resume: str, jobs: list[str]):
    resume_emb = model.encode(resume, convert_to_tensor=True)
    job_embs = model.encode(jobs, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(resume_emb, job_embs)[0]
    results = [
        {"job": job, "score": round(float(score), 2)}
        for job, score in zip(jobs, scores)
    ]
    return sorted(results, key=lambda x: x["score"], reverse=True)
