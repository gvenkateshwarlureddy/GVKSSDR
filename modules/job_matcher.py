from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def match(resume, job):
    r = model.encode(resume, convert_to_tensor=True)
    j = model.encode(job, convert_to_tensor=True)
    return float(util.cos_sim(r, j))