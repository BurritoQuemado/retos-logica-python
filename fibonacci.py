LIMIT = 50

n0 = 0
n1 = 1
for i in range(LIMIT):
    print(n0)
    fib = n0 + n1
    n0 = n1
    n1 = fib