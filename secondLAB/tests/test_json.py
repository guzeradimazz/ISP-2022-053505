from types import MappingProxyType
from parsers.jsonSerializer import JsonSerializer


def div(a, b):
    return a / b

def test_loads():
    serializer = JsonSerializer()
    serialized = serializer.dumps(serializer)
    serializer = serializer.loads(serialized)

def test_func():
    serializer = JsonSerializer()
    serialized = serializer.dumps(div)
    res = serializer.loads(serialized)
    assert res(4, 2) == 4/2

def test_mapping():
    serializer = JsonSerializer()
    item = {'key': 8, 'second_key': 9}
    mpt = MappingProxyType(item)
    serialized = serializer.dumps(mpt)
    serializer.loads(serialized)