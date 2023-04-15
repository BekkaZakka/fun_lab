def func(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    return x ** 3

def g(x):
    return x - 1

h = func(f, g)

result = h(4)
print(result)