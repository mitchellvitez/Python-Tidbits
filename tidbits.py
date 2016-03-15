import time

def chained_comparisons(x, y, z, pi=3.14):
    if 12 < x < 144:
        print x
    print 3 != x < y == 24 < z < 1000 > pi

def temp_swap(a, b):
    print a, b
    temp = a
    a = b
    b = a
    print a, b

def xor_swap(a, b):
    print a, b
    a ^= b
    b ^= a
    a ^= b
    print a, b

def tuple_swap(a, b):
    print a, b
    a, b = b, a
    print a, b

def slicing(s='Michigan Hackers'):
    print s[6:13]
    print s[:-5]
    print s[-5:]
    print s[::2]
    print s[::-1]

def cubes_imperative(n):
    cubes = []
    for x in range(n):
        cubes.append(x ** 3)
    print cubes

def cubes_functional(n):
    cubes = map(lambda x: x ** 3, range(n))
    print cubes

def cubes_comprehension(n):
    cubes = [x ** 3 for x in range(n)]
    print cubes

def two_dice_imperative():
    table = []
    for i in range(1, 7):
        row = []
        for j in range(1, 7):
            row.append(i + j)
        table.append(row)
    print table

def two_dice_comprehension():
    print [[i + j for i in range(1, 7)] for j in range(1, 7)]

def abracadabra(word):
    print [word[:i] for i in range(len(word), 0, -1)]

def increase(num, how_much=1, multiply=False):
    if multiply:
        return num * how_much
    return num + how_much

def increase_things():
    print increase(1)
    print increase(10, 10, False)
    increase(25, multiply=True, how_much=2)

def print_args(**kwargs):
    for arg in kwargs:
        print arg

def set_options():
    options = {
        'is_the_splab_door_open': True,
        'is_it_hack_night_yet': False,
        'students_enrolled_at_umich': 43651,
        'fishythefish_status': 'savage'
    }
    print_args(**options)

def add(a, b):
    return a + b

def add_list():
    nums = [1, 2]
    print add(*nums)

def sum(*nums):
    result = 0
    for num in nums:
        result += num
    return result

def take_sum():
    print sum(1, 2, 3, 4)

def args_func(arg1, arg2, *args, **kwargs):
    pass

def head_tail(things):
    x, xs = things[0], things[1:]
    print x, xs
    """
    x, *xs = things # Works in Python 3
    print x, xs
    """

class simple_range_list:
    def __init__(self, n):
        t0 = time.time()
        self.n = n
        self.data = [i for i in range(n)]
        print 'Time taken:', time.time() - t0

    def __iter__(self):
        return iter(self.data)

class simple_range_fast:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            result = self.i
            self.i += 1
            return result
        else:
            raise StopIteration()

def simple_range_genr(n):
    i = 0
    while i < n:
        yield i
        i += 1

def simple_ranges():
    simple_range_list(100000000) # Like range
    simple_range_fast(100000000) # Like xrange, or Python 3 range
    simple_range_genr(100000000)

def cubes_generator(n):
    print (x ** 3 for x in range(n))

def alphagen(start, end=None):
    s = list(reversed(start))
    
    while end is None or s != list(reversed(end)):
        yield ''.join(reversed(s))

        if s == list('z' * len(s)):
            s = list('a' * (len(s) + 1))

        else:
            for i, ch in enumerate(s):
                if ch is 'z':
                    s[i] = 'a'
                else:
                    s[i] = chr(ord(ch) + 1)
                    break

def count_strings_between(a, b):
    i = 0
    for s in alphagen(a, b):
        i += 1
    print i - 1

def fibonacci_traced(n):
    t0 = time.time()
    print 'fib started'

    if n is 0 or n is 1:
        print 'fib finished in', time.time() - t0, 'seconds returning', 1
        return 1

    else:
        x = fibonacci(n-1) + fibonacci(n-2)
        print 'fib finished in', time.time() - t0, 'seconds returning', x
        return x

def trace(f):
    def f_prime(n):
        t0 = time.time()
        print f.__name__, 'started'
        value = f(n)
        print f.__name__, 'finished in', time.time() - t0, 'seconds returning', value
        return value
    return f_prime

@trace
def fibonacci(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def comma_separate(s):
    words = s.split()
    s = ', '.join(words)
    print s

def pick_a_player(players):
    import random
    random.choice(players)
