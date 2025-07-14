#examples
def func():
    print("Começo da função")

    yield

    print("Fim da função")

try:
    y = func()
    next(y)
    next(y)

except StopIteration as e:
    pass


#computations
def func():
    x = 5
    print("Começo da função")

    yield x
    x += 7
    print("Meio da função")

    yield x

    print("Fim da função")

try:
    y = func()

    z = next(y)
    print(z)

    z = next(y)
    print(z)

    z = next(y)
    print(z)

except StopIteration as e:
    pass

#Send-values
def func():
    print("Começo da função")

    x = yield
    print(x)
    print("Meio da função")

    a = yield
    print(a)
    print("Fim da função")

try:
    y = func()

    next(y)

    y.send(5)
    y.send(8)

except StopIteration as e:
    pass

#multiple

def func():
    print('Função 1 começo')

    yield
    print('Funcão 1 Meio')

    yield
    print('Funcão 1 Fim')

def func2():
    print('Função 2 começo')

    yield
    print('Funcão 2 Meio')

    yield
    print('Funcão 2 Fim')

try:

    a = func()
    b = func2()

    next(a)
    next(b)
    next(b)
    next(a)
    next(a)
    next(b)

except StopIteration as e:
    pass