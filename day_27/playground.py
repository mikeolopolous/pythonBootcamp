# Uso de *args
def add(*args):
    suma = 0
    for num in args:
        suma += num

    return suma


print(add(2, 5, 8))


# Uso de **kwargs
def calculate(n, **kwargs):
    print(kwargs)

    suma = n + kwargs["add"]
    multiplicacion = n * kwargs["multiply"]

    return suma, multiplicacion


print(calculate(2, add=3, multiply=5))
