from parsers.parserParent import Serializer
import toml

class TomlSerializer(Serializer):

    def dumps(self, obj):
        obj_dict = super().dumps(obj)
        if 'code' in obj_dict:
            for (key, value) in obj_dict['code'].items():
                if key == 'co_consts':
                    value = list(value)
                    obj_dict['code'][key] = value

        return toml.dumps(obj_dict)

    def loads(self, toml_string):
        return super().loads(toml.loads(toml_string))