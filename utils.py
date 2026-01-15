import re, string

def clean_text(t):
    t = t.lower()
    t = re.sub(r"http\S+", " ", t)
    t = t.translate(str.maketrans("", "", string.punctuation))
    t = re.sub(r"\d+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()