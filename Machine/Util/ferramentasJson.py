import json


def lerJson(nomeAqr: str) -> any:
    with open(f"../{nomeAqr}") as j:
        data = json.load(j)
        return data
        
#print(lerJson('mt.json'))