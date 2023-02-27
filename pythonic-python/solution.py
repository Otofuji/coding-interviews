def print_indices_and_elements(elements) -> None:
    count = 0
    indices = 0
    for count, indices in enumerate(elements): #https://realpython.com/python-enumerate/
        print(count, indices)
    
def get_even_numbers_between(start: int, end: int) -> list[int]:
    #https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
    end += 1
    sequence = list(range(start, end)) #https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values
    even = [n for n in sequence if n%2 == 0]
    return even


def get_char_set_from(s: str) -> set[str]:
    ___set___ = set()
    ___set___ = {c for c in s}
    return ___set___


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {k:int(k**0.5) for k in range(start, end+1) if int(k**0.5)**2 == k}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n%2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [-1 if n % 2 != 0 else n for n in numbers if n % 5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    if version == 1:
        return "generator"
    elif version == 2:
        return "list"

def fibonacci1(n):
    prev = 1
    curr = 1
    yield 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        yield curr

def fibonacci2(n):
    result = [1]
    prev = 1
    curr = 1
    for _ in range(n-1):
        prev, curr = curr, curr + prev
        result.append(curr)
    return result

def difference_between_fibonacci1_and_fibonacci2() -> str:
    import sys
    import matplotlib.pyplot as plt
    memory_usage_fib1 = []
    memory_usage_fib2 = []

    for i in range(1, 1001):
        memory_usage_fib1.append(sys.getsizeof([f for f in fibonacci1(i)]))
        memory_usage_fib2.append(sys.getsizeof(fibonacci2(i)))

    plt.plot(memory_usage_fib1, label='fibonacci1')
    plt.plot(memory_usage_fib2, label='fibonacci2')
    plt.xlabel('n')
    plt.ylabel('Memory usage')
    plt.legend()
    plt.show()

    return "fibonacci1 uses a generator to lazily generate the sequence one value at a time, which is more memory-efficient than fibonacci2 that stores the entire sequence in a list. However, fibonacci1 can be slower than fibonacci2 for small sequences, due to the overhead of generating values on the fly. For large sequences, fibonacci1 can be faster and more memory-efficient than fibonacci2, because it doesn't need to store the entire sequence in memory at once. Este exercício é alienígena. Muito difícil. Ele foi feito com ajuda do ChatGPT."

class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.elements):
            raise StopIteration()
            
        element = self.elements[self.index]
        self.index += 2
        return element


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    nums = [e1, e2] + list(others)
    return sum(nums) / len(nums)


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c1 = {**a, **b}
    c2 = {**b, **a}
    
    keys = []
    for key in sorted(c1.keys()):
        if c1[key] != c2[key]:
            keys.append(key)
            
    return keys


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        first, *middle, last = numbers
        print(first, last)
        numbers = middle

    if numbers:
         print(numbers[0])  


def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    # You may add code here
    if to is None:
        to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
