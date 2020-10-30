cache = [1, 1]


def fib(x):
    if x <= 1:
        return 1
    if len(cache) <= x:
        cache.append(fib(x - 1) + fib(x - 2))

    return cache[x]


for i in range(50):
    print(fib(i))
