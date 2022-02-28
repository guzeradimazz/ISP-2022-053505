import argparse
import re

class Main:

    def parce():
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

        core_average = core.get_average_essense()
        core_median = core.get_median_essense()


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
    
    def get_average_essense(self) -> tuple[float, float]:
        averages = re.split(r'\.|!|\?', self.text)
        averages = list(filter(lambda average: average != '', averages))
        all_average = [len(average.split()) for average in averages]
        return TextCore.get_average(all_average)

    def get_median_essense(self) -> tuple[float, float]:
        medians = re.split(r'\.|!|\?', self.text)
        medians = list(filter(lambda median: median != '', medians))
        all_median = [len(median.split()) for median in medians]
        return TextCore.get_median(all_median)


Main.main()