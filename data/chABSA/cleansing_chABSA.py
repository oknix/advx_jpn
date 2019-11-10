import pandas as pd
from pathlib import Path
import json

def create_rating(sentences):
    rating = []
    for obj in sentences:
        s = obj["sentence"]
        op = obj["opinions"]
        porarity = 0
        for o in op:
            p = o["polarity"]
            if p == "positive":
                porarity += 1
            elif p == "negative":
                porarity -= 1
        if porarity !=0 :
            rating.append((porarity, s))
    return rating

# パスの読み込み
data_dir = "data/chABSA/chABSA-dataset/"
data_path = Path(data_dir)
path_list = [p for p in data_path.iterdir() if ".json" in str(p)]

print(len(path_list))
#print(path_list[:5])

with open(path_list[0], "br") as f:
    j =  json.load(f)
sentences = j["sentences"]

rating = []
for p in path_list:
    with open(p, "br") as f:
        j =  json.load(f)
    s = j["sentences"]
    rating += create_rating(s)

neg =[]
pos = []
for t in rating:
    if t[0] > 0:
        pos.append(t[1])
    else:
        neg.append(t[1])

with open("data/chABSA/neg.txt", "w") as f:
    for s in neg:
        r = s + "\n"
        f.write(r)

with open("data/chABSA/pos.txt", "w") as f:
    for s in pos:
        r = s + "\n"
        f.write(r)
