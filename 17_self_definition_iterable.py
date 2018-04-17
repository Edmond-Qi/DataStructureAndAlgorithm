# coding：utf-8
from collections import Iterator
from collections import Iterable


# 迭代器对象
class OwnIterator(Iterator):
    def __init__(self, arrs):
        self.index = 0
        self.arrs = arrs

    def __next__(self):
        if self.index > len(self.arrs) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.arrs[self.index - 1]


class OwnIterable(Iterable):
    def __init__(self, arrs):
        self.arrs = arrs

    def __iter__(self):
        return OwnIterator(self.arrs)


for item in OwnIterable([1, 2, 3, 4, 4, 5]):
    print(item)
