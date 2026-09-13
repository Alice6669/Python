def multiplicador(*args):
    multiplicaoTotal = 1
    for numero in args:
        multiplicaoTotal *= numero
    return multiplicaoTotal

print(multiplicador(10,2,4,5))