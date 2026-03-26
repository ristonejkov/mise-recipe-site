import json

with open("recipes_small.json") as f:
    data = json.load(f)

for r in data:
    r["ingredients"] = json.loads(r["ingredients"])
    r["directions"] = json.loads(r["directions"])

with open("recipes_normalized.json","w") as f:
    json.dump(data,f)