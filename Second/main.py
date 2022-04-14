from customSerializator import Serializator
from patternFactory import FabricSerializator


def getSerializator(type):
    tempSerializator = Serializator()
    if type == 'Json': tempSerializator = FabricSerializator.serializator('Json')
    elif type == 'Yaml': tempSerializator = FabricSerializator.serializator('Yaml')
    elif type == 'Toml': tempSerializator = FabricSerializator.serializator('Toml')
    return tempSerializator

lamdaFunction = lambda x,y: x+2*y

def funcForSerializator(props):
    print(props)
    return props+10

dictForSerializaotr = {'a': 1, 'b': 2}


if __name__=="__main__":

    ######JSON#####
    getSerializator("Json")().dump(funcForSerializator, "./func.json")

    # jsonObj = getSerializator("Json").loads(getSerializator("Json")().dumps(lamdaFunction))
    # # print(jsonObj(2, 3))

    # getSerializator("Json").dump(funcForSerializator, "func1.json")
    # func1 = getSerializator("Json").load('func1.json')

    
    # getSerializator("Json")().loads(getSerializator("Json")().dumps(dictForSerializaotr))
    ######JSON#####