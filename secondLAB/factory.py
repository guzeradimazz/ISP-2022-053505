from parsers import jsonSerializer,yamlSerializer,tomlSerializer


class SerializerFabric:
    def createSerializer(): pass

class JsonSerializerFabric(SerializerFabric):
    def createSerializer(): return jsonSerializer.JsonSerializer()

class YamlSerializerFabric(SerializerFabric):
    def createSerializer(): return yamlSerializer.YamlSerializer()
    
class TomlSerializerFabric(SerializerFabric):
    def createSerializer(): return tomlSerializer.TomlSerializer()