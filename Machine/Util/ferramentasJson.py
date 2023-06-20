import json

class ConvertJson:
    @staticmethod
    def lerJson(nomeAqr: str) -> any:
        with open(f"{nomeAqr}") as j: #f"../{nomeAqr}"
            data = json.load(j)
            return data
        
#print(lerJson('mt.json'))