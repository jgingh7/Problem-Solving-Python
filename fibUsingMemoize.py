def memoize(f):
    print("memo")
    store = {}
    def anon(x):
        if store.has_key(x):
            print ("inif")
            return store[x]
        else:
            y = f(x)
            store[x] = y
            print(store)
            return y
    print("memo out")
    return anon


def fib(n):
    print("fib({})".format(n))
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Before_Start")
fib = memoize(fib)
print("Start")

print(fib (5))
