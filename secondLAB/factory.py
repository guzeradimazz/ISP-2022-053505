from parsers import json_Serializer,yamlSerializer,tomlSerializer


class SerializerFabric:
    def createSerializer(): pass

class JsonSerializerFabric(SerializerFabric):
    def createSerializer(): return json_Serializer.JsonSerializer()

class YamlSerializerFabric(SerializerFabric):
    def createSerializer(): return yamlSerializer.YamlSerializer()
    
class TomlSerializerFabric(SerializerFabric):
    def createSerializer(): return tomlSerializer.TomlSerializer()