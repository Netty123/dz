from datetime import datetime
from functools import wraps

def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            result = old_function(*args, **kwargs)
            
            log_entry = f'{date_time} - {old_function.__name__}, args={args}, kwargs={kwargs}, result={result}\n'
            
            with open(path, 'a', encoding='utf-8') as f:
                f.write(log_entry)
            
            return result
        return new_function
    return __logger


class FlatIterator:
    def __init__(self, list_of_list):
        self.data = list_of_list
        self.outer_index = 0
        self.inner_index = 0
        
        # Логируем создание итератора
        self._log_creation()

    def _log_creation(self):
        date_time = datetime.now()
        log_entry = f'{date_time} - FlatIterator.__init__, list_of_list length={len(self.data)}\n'
        
        with open('iterator.log', 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_index < len(self.data):
            current = self.data[self.outer_index]
            if self.inner_index < len(current):
                item = current[self.inner_index]
                self.inner_index += 1
                
                # Логируем возвращаемый элемент
                self._log_next(item)
                
                return item
            else:
                self.outer_index += 1
                self.inner_index = 0
        
        # Логируем остановку итерации
        self._log_stop()
        raise StopIteration
    
    def _log_next(self, item):
        date_time = datetime.now()
        log_entry = f'{date_time} - FlatIterator.__next__ -> {repr(item)} [outer={self.outer_index}, inner={self.inner_index-1}]\n'
        
        with open('iterator.log', 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    def _log_stop(self):
        date_time = datetime.now()
        log_entry = f'{date_time} - FlatIterator.__next__ -> StopIteration\n'
        
        with open('iterator.log', 'a', encoding='utf-8') as f:
            f.write(log_entry)


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


if __name__ == '__main__':
    test_1()