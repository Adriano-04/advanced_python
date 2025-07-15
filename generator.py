def gen():
    g = 1
    print('Primeiro')
    yield g

    g += 1
    print('Segundo')
    yield g

    g += 1
    print('Terceiro')
    yield g