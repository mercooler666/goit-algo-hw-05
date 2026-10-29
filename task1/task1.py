def caching_febonacci():
    chache = {}

    def febonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cahce[n]
    return febonacci()

fib = caching_febonacci()

print(fib(10))
print(fib(15))
