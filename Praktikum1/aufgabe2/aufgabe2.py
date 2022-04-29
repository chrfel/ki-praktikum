from json import loads
from pprint import pprint
import functools

def faku(n):
    if n == 0 or n == 1:
        return 1
    return faku(n-1)*n

def createFakultaetGenerator(n):
    num = 1
    while n > 0:
        yield num*n
        n -= 1

def create_generator():
    print("c")
    fakultaeten = range(10)
    num = 1
    for i in fakultaeten:
        print("a")
        num = num*(i+1)
        yield num

def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

if __name__ == "__main__": 
    # JSON
    print("JSON:")
    with open("aufgabe2/fruit.json") as file:
        fruit_dict = loads(file.read())
        pprint(fruit_dict)
        for k,v in fruit_dict.items():
            pprint(f"{k}- {v}")

    # Generator
    print("Generator 3^x:")
    fakultaeten = (3**x for x in range(20))
    for i in fakultaeten:
        print(i)

    # Generator yield
    print("Fibonacci Generator Yield:")
    fakultaetenGenerator = create_generator()
    for i in fakultaetenGenerator:
        print("b")
        print(i)

    # Gemittelte Folgen
    print("Gemittelte Folgen:")
    n = 20
    gemittelt = [x for x in range(1,n)]
    print(gemittelt)
    print((1/n) * functools.reduce(lambda a, b: b, gemittelt))


    