import qtoml
import parsers.serializer_core as core
from parsers.parser_parent import Serializer

class TomlSerializer(Serializer):

    def dumps(self, item):
        return qtoml.dumps(core.serialize(item), encode_none=())

    def loads(self, string):
        return core.deserialize(qtoml.loads(string))