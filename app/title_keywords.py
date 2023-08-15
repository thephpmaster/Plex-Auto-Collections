import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
blacklist = stopwords.words('english')
blacklist.extend(["the", "part"])
blacklist = set(blacklist)
whitelist = set(["vr"])

def extract_kw(kw):
    kw = kw.strip().lower()
    if not kw:
        return None
    if kw not in whitelist:
        if kw in blacklist or len(kw) > 18 or len(kw) < 3 or kw.isnumeric():
            return None
    return kw.capitalize()
    

"""Extract any meaningful words from string"""
def keywords(title):
    keywords = re.split("_|\.|\W|\-", title)
    keywords = (extract_kw(kw) for kw in keywords)
    keywords = set(filter(bool, keywords))
    return keywords

if __name__ == "__main__":
    names = u"""
Toy Story 3 
Toy Story 2 
Toy Story 1 
Harry Potter and the Deathly Hallows: Part 1
Harry Potter and the Philosopher's Stone
Harry Potter and the Order of the Phoenix
Alice in Wonderland
Star Wars: Episode I - The Phantom Menace
Jurassic Park
The Land Before Time
Pirates of the Caribbean: On Stranger Tides
Pirates of the Caribbean: Dead Man's Chest
Pirates of the Caribbean: At World's End
"""
    lines = [line.strip() for line in names.split("\n") if line.strip()]
    for line in lines:
        print("{0: <60} -> {1}".format(line, ", ".join(keywords(line))))