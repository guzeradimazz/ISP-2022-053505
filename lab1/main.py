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
        k, n = 10, 4
        core = TextCore(Main.get_text())
        core_true_words = core.all_core_words()
        print(core_true_words)

        print("Average count of words")
        print(f"> {core.get_average_essense()}")
        print("Median is equal")
        print(f"> {core.get_median_essense()}")

        print("Full n-grams")
        repeatable_top_essense = core.repeatable_top(k,n)
        Main.print_method(repeatable_top_essense)

class TextCore:
    def __init__(self,text:str) ->None:
        self.text = text

    def core_counter(self, items):
        core = dict()
        for i in items:
            core[i] = core.get(i, 0) + 1
        true_items = sorted(core.items(),
                              key=lambda i: i[1],
                              reverse=True
                              )
        core = dict(true_items)
        return core

    def all_core_words(self):
        words = re.split("[^a-zа-я']", self.text.lower())
        words = list(filter(lambda word: word != '', words))
        return self.core_counter(words)
    
    def get_average(numbers):
        if numbers:
            return sum(numbers)/len(numbers)
        else: return 0

    def get_median(numbers):
        if numbers:
            length = len(numbers)
            if(length & 1 == 0):
                result = numbers[int(length/2)]+numbers[int(length/2)+1]
                result /= 2
            else:
                result = numbers[int(length/2)]
            return result
        else: return 0
    
    def get_average_essense(self):
        averages = re.split(r'\.|!|\?', self.text)
        averages = list(filter(lambda average: average != '', averages))
        all_average = [len(average.split()) for average in averages]
        return TextCore.get_average(all_average)

    def get_median_essense(self):
        medians = re.split(r'\.|!|\?', self.text)
        medians = list(filter(lambda median: median != '', medians))
        all_median = [len(median.split()) for median in medians]
        return TextCore.get_median(all_median)

    def repeatable_top(self, k: int = 10, n: int = 4):
        temp_list = re.split("[^a-zа-я]", self.text.lower())
        temp_list = list(filter(lambda w: len(w) >= n, temp_list))
        ngrams = list()
        for w in temp_list:
            ngrams_in_word = list(zip(*[w[i:] for i in range(n)]))
            for j in ngrams_in_word:
                ngrams.append(''.join(j))
        ngrams_count = self.core_counter(ngrams)
        return dict(list(ngrams_count.items())[:k])

Main.main()