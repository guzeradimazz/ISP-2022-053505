import qtoml
import parsers.serializerCore as core
from parsers.parserParent import Serializer

class TomlSerializer(Serializer):

    def dumps(self, item):
        return qtoml.dumps(core.serialize(item), encode_none=())

    def loads(self, string):
        return core.deserialize(qtoml.loads(string))