from parsers.parserParent import Serializer
import parsers.serializerCore as core


class JsonSerializer(Serializer):

    def dumps(self, item):
        def toString(item):
            if isinstance(item, dict):
                strings = list()
                for key, value in item.items():
                    strings.append(f'{toString(key)}:{toString(value)},')
                return f"{{{''.join(strings)[:-1]}}}"
            elif isinstance(item, str):
                string = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return f"\"{string}\""
            elif item is None:return 'null'
            else:return str(item)
        return toString(core.serialize(item))

    def loads(self, string):
        null = None
        return core.deserialize(eval(string))