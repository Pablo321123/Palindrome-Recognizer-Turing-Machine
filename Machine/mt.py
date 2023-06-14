import sys
from Util import ferramentasJson

def lerArgs(args):
    nomeJson = args[1]
    palavra = args[2]
    data = ferramentasJson.lerJson(nomeJson)
    print(nomeJson)
    print(palavra)
    print(data)


# Passo os argumentos recebidos pelo terminal como parametro separados por ' '.
lerArgs(sys.argv)
