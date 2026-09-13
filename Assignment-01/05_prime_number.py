# Program 5: Prime Number

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if isPrime(num):
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
