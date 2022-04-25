from factory import JsonSerializerFabric,YamlSerializerFabric,TomlSerializerFabric
import math

class Animal:
    def __init__(self, color='red', weight=100):
        self.color = color
        self.weight = weight

    color: str
    weight:int

    animalTuple = tuple('animal tuple by letter')

    animalList = ['a','r','r','a','y',' ','i','n',' ','J','S']

    animalDict = {
        "This": "Is",
        "Object": "In",
        "JavaScript": 228
    }

    animalLambda = lambda x:x*5

    def multipleWeight(self): return 5*self.weight


def main():
    menu = input()
    entity = Animal('brown',200)

    if(menu == '1'):
        parser = JsonSerializerFabric.createSerializer()
        parser.dump(entity,'./utils/entity.json')
        parser.load('./utils/entity.json')
    elif(menu == '2'):
        parser = YamlSerializerFabric.createSerializer()
        parser.dump(entity,'./utils/entity.yaml')
        parser.load('./utils/entity.yaml')
    elif(menu == '3'):
        parser = TomlSerializerFabric.createSerializer()
        parser.dump(entity,'./utils/entity.toml')
        parser.load('./utils/entity.toml')
    else: raise Exception('Invalid menu')

main()