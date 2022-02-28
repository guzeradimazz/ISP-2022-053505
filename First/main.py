import argparse
import re

class Main:

    def parce():
        """Run parcer and get args."""
        parcer = argparse.ArgumentParser(description='Process input')
        parcer.add_argument('-n', type=int, default=4, help='legth of n-gram')
        parcer.add_argument(
            '-k',
            type=int,
            default=10,
            help='number of top n-grams to display'
        )
        parcer.add_argument(
            'filename',
            type=argparse.FileType('r'),
            nargs='?',
            default="text.txt",
            help='file to read'
        )
        return parcer.parse_args()

    def print_method(dictionaty: dict) ->None:
        for (i,j) in dictionaty.items():
            print(f'{i}:{j}')

    def get_text() ->str:
        args = Main.parce()
        return args.filename.read()

    def main():
        text = Main.get_text()
        core = TextCore(text)
        core_true_words = core.all_core_words()
        print(core_true_words)


class TextCore:
    def __init__(self,text:str) ->None:
        self.text = text

    def core_counter(self, items: list) ->dict[any, int]:
        core = dict()
        for i in items:
            core[i] = core.get(i, 0) + 1
        true_items = sorted(core.items(),
                              key=lambda i: i[1],
                              reverse=True
                              )
        core = dict(true_items)
        return core

    def all_core_words(self) ->dict[str, int]:
        words = re.split("[^a-zа-я']", self.text.lower())
        words = list(filter(lambda word: word != '', words))
        return self.core_counter(words)
    
    def get_average(numbers :list[int]) ->int:
        return sum(numbers)/len(numbers)

    def get_median(numbers: list[int]) ->int:
        length = len(numbers)
        if(length & 1 == 0):
            result = numbers[int(length/2)]+numbers[int(length/2)+1]
            result /= 2
        else:
            result = numbers[int(length/2)]
        return result
    


Main.main()