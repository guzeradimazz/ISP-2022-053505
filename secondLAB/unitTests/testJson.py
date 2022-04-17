from types import MappingProxyType
from parsers.jsonSerializer import jsonSerializer
import unittest

def func(a, b):
    return a * b

class TestJson(unittest.TestCase):

    def testLoads():
        serializer = jsonSerializer()
        s = serializer.dumps(serializer)
        serializer = serializer.loads(s)


    def testFunction():
        serializer = jsonSerializer()
        s = serializer.dumps(func)
        res = serializer.loads(s)
        assert res(6, 8) == 8*6


    def testMain():
        serializer = jsonSerializer()
        item = {'item': 8, 'item2': 9}
        mpt = MappingProxyType(item)
        s = serializer.dumps(mpt)
        serializer.loads(s)

if __name__ == '__main__':
    unittest.main()