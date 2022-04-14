class Serializer:

    def dumps(self, item):
        pass

    def loads(self, string):
        pass

    def dump(self, item, filename):
        file = open(filename, 'w')
        file.write(self.dumps(item))

    def load(self, filename):
        file = open(filename, 'r')
        return self.loads(file.read())