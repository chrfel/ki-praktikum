from json import loads
from pprint import pprint
import functools

def faku(n):
    if n == 0 or n == 1:
        return 1
    return faku(n-1)*n

def create_generator():
    fakultaeten = range(10)
    for i in fakultaeten:
        yield faku(i)

def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

if __name__ == "__main__": 
    # JSON
    with open("aufgabe2/fruit.json") as file:
        fruit_dict = loads(file.read())
        pprint(fruit_dict)

    # Generator
    print("Generator 3^x:")
    fakultaeten = (3**x for x in range(10))
    for i in fakultaeten:
        print(i)

    # Generator yield
    print("Fibonacci Generator Yield:")
    fakultaetenGenerator = create_generator()
    for i in fakultaetenGenerator:
        print(i)

    # Gemittelte Folgen
    n = 20
    gemittelt = [x for x in range(1,n)]
    print(gemittelt)
    print((1/n) * functools.reduce(lambda a, b: a+b, gemittelt))


    