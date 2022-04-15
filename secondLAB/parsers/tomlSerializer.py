from parsers.parserParent import Serializer
import toml

class TomlSerializer(Serializer):

    def dumps(entity,path):
        return toml.dumps(entity,path)

    def loads(entity):
        return toml.loads(entity)
