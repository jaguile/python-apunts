def comptador(límit):
    actual = 0
    while actual < límit:
        yield actual
        actual += 1

for x in comptador(3):
    print(x)
