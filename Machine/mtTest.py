import sys
from Util import ferramentasJson
from machine import MaquinaTuring


def lerArgs(args):
    try:
        nomeJson = 'mt.json'  # args[1]
        palavra = '001100'  # args[2]
        data = ferramentasJson.ConvertJson.lerJson(nomeJson)        
    except Exception as e:
        print(e)
        
    return data, palavra
    
    

if __name__ == "__main__":
    # Passo os argumentos recebidos pelo terminal como parametro separados por ' '.
    data = lerArgs(sys.argv)
    MaquinaTuring(data[0]['mt'][0], data[0]['mt'][1], data[0]['mt'][2], data[0]['mt'][3], data[0]['mt'][4],
                         data[0]['mt'][5], data[0]['mt'][6], data[0]['mt'][7], data[0]['mt'][8], data[1])
