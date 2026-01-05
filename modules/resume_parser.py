import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(text):
    data = {}

    # Email
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    data["email"] = email[0] if email else ""

    # Phone
    phone = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)
    data["phone"] = phone[0] if phone else ""

    # Name (first PERSON entity)
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            parts = ent.text.split()
            data["first_name"] = parts[0]
            data["last_name"] = parts[-1] if len(parts) > 1 else ""
            break

    # Skills (simple keyword capture)
    skills = []
    for token in doc:
        if token.pos_ == "NOUN" and len(token.text) > 3:
            skills.append(token.text)

    data["skills"] = list(set(skills))[:15]

    return data