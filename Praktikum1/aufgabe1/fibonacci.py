def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-2)+fibo(n-1)

if __name__ == "__main__": 
    print(fibo(10))