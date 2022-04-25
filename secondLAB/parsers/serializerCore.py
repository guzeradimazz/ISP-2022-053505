import types
from inspect import getmodule
import sys
import importlib
import builtins
import __main__


def serialize(item):

    def serialize_elements(item):
        elements = {}
        for i, element in enumerate(item):
            elements[f"el{i}"] = serialize(element)
        return elements

    def serialize_pub_attribs(item):
        elements = {}
        pub_attributes = list(
            filter(lambda item: not item.startswith('_'), dir(item)))
        for attr in pub_attributes:
            elements[attr] = serialize(item.__getattribute__(attr))
        return elements

    if isinstance(item, int | str | types.NoneType): return item
    if isinstance(item, tuple): return {"tuple": serialize_elements(item)}
    if isinstance(item, list): return {"list": serialize_elements(item)}
    if isinstance(item, dict): return {"dict": item}
    if isinstance(item, bytes): return {"bytes": item.hex()}
    if isinstance(item, types.MappingProxyType):
        item_dict = dict(item)
        for key in item_dict.keys():
            item_dict[key] = serialize(item_dict[key])
        print("hello")
        return item_dict

    if isinstance(item, types.CodeType): return {"code": serialize_pub_attribs(item)}
    if isinstance(item, types.FunctionType): return {"func": serialize(item.__code__)}
    if isinstance(item, type):
        attribs_dict = dict(item.__dict__)
        for key in attribs_dict.keys():
            attribs_dict[key] = serialize(attribs_dict[key])
        attribs_dict['__annotations__'] = None
        return {"type": {"name": item.__name__, "attribs": attribs_dict}}

    if (getmodule(type(item)).__name__ in sys.builtin_module_names or
        getmodule(type(item)).__name__ == 'importlib._bootstrap' or
            getmodule(type(item)).__name__ == '_sitebuiltins'):
        return None

    obj_dict = serialize(item.__dict__)
    obj_type = serialize(type(item))
    return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}


def deserialize(item: dict[str, any]):
    if not isinstance(item, dict): return item

    for (key, value) in item.items():
        if key == 'tuple':
            if value is None:
                return ()
            return tuple(deserialize(element) for element in value.values())
        if key == 'list': return [deserialize(element) for element in value.values()]
        if key == 'dict': return value
        if key == 'bytes': return bytes.fromhex(value)
        if isinstance(value, int | float | str): return value
        if key == 'type':
            globals().update(__main__.__dict__)

            obj_type = getattr(__main__, value['name'], None)
            serialized = serialize(obj_type)

            if(serialized is None
               or isinstance(serialized, dict)
               and serialized['type'] != value):
                attribs = value['attribs']
                for i in attribs.keys():
                    attribs[i] = deserialize(attribs[i])

                obj_type = type(
                    value['name'],
                    (object, ),
                    attribs
                )

            return obj_type

        if key == 'func':

            f_code = deserialize(value)

            def func():
                pass
            func.__code__ = f_code
            return func

        if key == 'code':
            code_names = deserialize(value["co_names"])

            for name in code_names:
                if builtins.__dict__.get(name, 42) == 42:
                    try:
                        builtins.__dict__[name] = importlib.import_module(name)
                    except ModuleNotFoundError:
                        builtins.__dict__[name] = 42

            return types.CodeType(
                deserialize(value["co_argcount"]),
                deserialize(value["co_posonlyargcount"]),
                deserialize(value["co_kwonlyargcount"]),
                deserialize(value["co_nlocals"]),
                deserialize(value["co_stacksize"]),
                deserialize(value["co_flags"]),
                deserialize(value["co_code"]),
                deserialize(value["co_consts"]),
                code_names,
                deserialize(value["co_varnames"]),
                "deserialized",
                deserialize(value["co_name"]),
                deserialize(value["co_firstlineno"]),
                deserialize(value["co_lnotab"]),
                deserialize(value["co_freevars"]),
                deserialize(value["co_cellvars"])
            )
        if key == 'object':
            obj_type = deserialize(value['obj_type'])
            obj_dict = deserialize(value['obj_dict'])

            try:
                obj = object.__new__(obj_type)
                obj.__dict__ = obj_dict
                for (obj_key, obj_value) in obj_dict.items():
                    setattr(obj, obj_key, obj_value)
            except TypeError:
                obj = None
            return obj

    return None