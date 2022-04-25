from types import MappingProxyType
from parsers.jsonSerializer import JsonSerializer
import math

def div(a, b):
    return a / b

c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)

def test_loads():
    serializer = JsonSerializer()
    serialized = serializer.dumps(serializer)
    serializer = serializer.loads(serialized)

def test_func():
    serializer = JsonSerializer()
    serialized = serializer.dumps(f)
    res = serializer.loads(serialized)
    assert res(4) == math.sin(4 * 123 * 42)

def test_mapping():
    serializer = JsonSerializer()
    item = {'key': 8, 'second_key': 9}
    mpt = MappingProxyType(item)
    serialized = serializer.dumps(mpt)
    serializer.loads(serialized)