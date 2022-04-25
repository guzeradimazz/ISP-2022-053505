from parsers.parser_parent import Serializer
import parsers.serializer_core as core


class JsonSerializer(Serializer):

    def dumps(self, item):
        def to_String(item):
            if isinstance(item, dict):
                strings = list()
                for key, value in item.items():
                    strings.append(f'{to_String(key)}:{to_String(value)},')
                return f"{{{''.join(strings)[:-1]}}}"
            elif isinstance(item, str):
                string = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return f"\"{string}\""
            elif item is None:return 'null'
            else:return str(item)
        return to_String(core.serialize(item))

    def loads(self, string):
        null = None
        return core.deserialize(eval(string))