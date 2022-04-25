from parsers import json_serializer,yaml_serializer,toml_serializer


class SerializerFabric:
    def createSerializer(): pass

class JsonSerializerFabric(SerializerFabric):
    def createSerializer(): return json_serializer.JsonSerializer()

class YamlSerializerFabric(SerializerFabric):
    def createSerializer(): return yaml_serializer.YamlSerializer()
    
class TomlSerializerFabric(SerializerFabric):
    def createSerializer(): return toml_serializer.TomlSerializer()