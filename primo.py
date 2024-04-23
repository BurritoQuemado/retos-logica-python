LIMIT = 100

def isPrime(number):
    if number < 2:
        return False
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
    return True

for i in range(LIMIT):
    if isPrime(i):
        print(i)