# Fibonacci by recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Fibonacci by memoization
dic = {}
def fib2(n):
    if n in dic:
        return dic[n]

    if n==0:
        dic[0] = 0
        return 0
    elif n==1:
        dic[1] = 1
        return 1
    else:
        dic[n] = fib2(n-1) + fib2(n-2)
        return dic[n]

print(fib(20))
print(fib2(20))
