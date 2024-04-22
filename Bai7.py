from math import sqrt


def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


a = int(input("Enter a number: "))
if isprime(a):
    print(a, " la so nguyen to.")
else:
    print(a, " khong phai la so nguyen to.")
