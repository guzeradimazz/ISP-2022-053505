from parsers.parserParent import Serializer
import parsers.serializerCore as core
import toml

class TomlSerializer(Serializer):


    def dumps(self,entity):
        dictEntity = super().dumps(entity)
        if 'code' in dictEntity:
            for (key, value) in dictEntity['code'].items():
                if key == 'co_consts':
                    value = list(value)
                    dictEntity['code'][key] = value
        return toml.dumps(dictEntity)

    def loads(self,entity):
        return super().loads(toml.loads(entity))


    # def dumps(self,item):

    #     def toString(item,depth=0):
    #         if isinstance(item, dict):
    #             strings = list()
    #             prefix = '  '*depth

    #             if (False or isinstance(value, dict)
    #                     for value in item.values()):
    #                 prefix = '\n' + prefix
    #             for key, value in item.items():
    #                 strings.append(f'{prefix}{toString(key)}: {toString(value, depth+1)}')
    #             return ''.join(strings)
    #         elif isinstance(item, str):
    #             s = item.translate(str.maketrans({
    #                 "\"": r"\"",
    #                 "\\": r"\\",
    #             }))
    #             return s
    #         elif item is None: return ''
    #         else: return str(item)

    #     return toString(core.serialize(item))

    