'''
1.Доработать класс FlatIterator. Должен получиться итератор,
который принимает список списков и возвращает их плоское представление, 
т.е последовательность состоящую из вложенных элементов.

3. * Написать итератор аналогичный итератору из задания 1,
но обрабатывающий списки с любым уровнем вложенности.
'''

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.curs = iter(self.list_of_list)
        self.stack = []
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.curs)
                while isinstance(item, list):
                    self.stack.append(self.curs)
                    self.curs = iter(item)
                    item = next(self.curs)
                return item
            except StopIteration:
                if self.stack:
                    self.curs = self.stack.pop()
                    continue
                else:
                    raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_1()
    test_3()