from parsers.parser_parent import Serializer
import parsers.serializer_core as core

class YamlSerializer(Serializer):

    def dumps(self, item):
        def toString(item, depth=0):
            if isinstance(item, dict):
                strings = list()
                prefix = '    '*depth

                if (False or isinstance(value, dict)
                        for value in item.values()):
                            if(depth != 0): prefix = '\n' + prefix
                for key, value in item.items():
                    strings.append(
                        f'{prefix}{toString(key)}: {toString(value, depth+1)}')
                return ''.join(strings)
            elif isinstance(item, str):
                s = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return s
            elif item is None:return ''
            else:return str(item)

        return toString(core.serialize(item))

    def loads(self, string):
        def getSerValue(key, sval):
            temp = sval
            if not key.endswith('bytes'):
                try:
                    temp = float(temp)
                    if temp.is_integer:temp = int(temp)
                except Exception:pass
            if temp == '': temp = None
            return temp

        def iter(string):
            temp = dict()
            splitted = string.split('\n')
            keys = list(filter((lambda a: a != '' and a[0] != ' '), splitted))
            finish = 0
            dvals = list()
            for i in range(len(keys)):
                start = splitted.index(keys[i], finish)
                if(i == len(keys) - 1): finish = len(splitted)
                else: finish = splitted.index(keys[i + 1], start)
                dvals.append(list(splitted[start+1:finish]))
            svals = [key.partition(': ')[2] for key in keys]
            keys = [key.partition(':')[0] for key in keys]
            dvals = ['\n'.join([s[2:] for s in e]) for e in dvals]
            for i in range(len(keys)):
                if len(dvals[i]) == 0: temp = temp | {keys[i]: getSerValue(keys[i], svals[i])}
                else: temp = temp | {keys[i]: iter(dvals[i])}
            return temp

        return core.deserialize(iter(string))