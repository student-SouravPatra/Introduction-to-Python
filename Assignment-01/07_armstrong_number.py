# Program 7: Armstrong Number

def checkArmstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == original


num = int(input("Enter a number: "))

if num >= 0 and checkArmstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
