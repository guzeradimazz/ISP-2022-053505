import sys
import types
from inspect import getmodule

def serialize(item):
    def serializeEntities(item):
        elements = dict()
        for i in range(len(item)):
            elements[f"el{i}"] = serialize(item[i])
        return elements

    def serializeProps(item):
        elements = dict()
        pub_attributes = list(
            filter(lambda item: not item.startswith('_'), dir(item)))
        for attr in pub_attributes: 
            elements[attr] = serialize(item.__getattribute__(attr))
        return elements

    if isinstance(item, int | str): return item
    elif isinstance(item, tuple): return {"tuple": serializeEntities(item)}
    elif isinstance(item, list): return {"list": serializeEntities(item)}
    elif isinstance(item, dict): return {"dict": item}
    elif isinstance(item, bytes): return {"bytes": item.hex()}
    elif isinstance(item, types.MappingProxyType):
        temp = dict(item)
        for key in temp.keys():
            temp[key] = serialize(temp[key])
        return temp
    elif isinstance(item, types.CodeType): return {"code": serializeProps(item)}
    elif isinstance(item, types.FunctionType): return {"func": serialize(item.__code__)}
    elif isinstance(item, type):
        temp = dict(item.__dict__)
        for key in temp.keys():
            temp[key] = serialize(temp[key])
        temp['__annotations__'] = None
        return {"type": {"name": item.__name__, "attribs": temp}}
    if (getmodule(type(item)).__name__ in sys.builtin_module_names):  return None
    if (getmodule(type(item)).__name__ == 'importlib._bootstrap'): return None
    if (getmodule(type(item)).__name__ == '_sitebuiltins'): return None
    else:
        obj_dict = serialize(item.__dict__)
        obj_type = serialize(type(item))
        return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}

def deserialize(item):
    if not isinstance(item, dict): return item
    for (key, value) in item.items():
        if(key == 'tuple'):
            if value is None: return ()
            return tuple([deserialize(element) for element in value.values()])
        elif(key == 'list'): return [deserialize(element) for element in value.values()]
        elif(key == 'dict'): return value
        elif(key == 'bytes'): return bytes.fromhex(value)
        elif(isinstance(value, int | float | str)): return value
        elif(key == 'type'):
            import __main__
            globals().update(__main__.__dict__)
            obj_type = getattr(__main__, value['name'], None)
            attribs = value['attribs']
            for key in attribs.keys():
                attribs[key] = deserialize(attribs[key])

            obj_type = type(
                value['name'],
                (object, ),
                attribs
            )
            return obj_type
        elif(key == 'func'):
            import __main__
            globals().update(__main__.__dict__)
            def func(): pass
            func.__code__ = deserialize(value)
            return func
        elif(key == 'code'):
            return types.CodeType(
                deserialize(value["co_argcount"]),
                deserialize(value["co_posonlyargcount"]),
                deserialize(value["co_kwonlyargcount"]),
                deserialize(value["co_nlocals"]),
                deserialize(value["co_stacksize"]),
                deserialize(value["co_flags"]),
                deserialize(value["co_code"]),
                deserialize(value["co_consts"]),
                deserialize(value["co_names"]),
                deserialize(value["co_varnames"]),
                "deserialized",
                deserialize(value["co_name"]),
                deserialize(value["co_firstlineno"]),
                deserialize(value["co_lnotab"]),
                deserialize(value["co_freevars"]),
                deserialize(value["co_cellvars"])
            )
        elif(key == 'object'):
            obj_type = deserialize(value['obj_type'])
            obj_dict = deserialize(value['obj_dict'])
            try:
                obj = object.__new__(obj_type)
                obj.__dict__ = obj_dict
                for (key, value) in obj_dict.items():
                    setattr(obj, key, value)
            except TypeError:
                obj = None
            return obj