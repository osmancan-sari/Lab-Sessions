import math
def is_prime(num:int):
    if num<=1:
        return False
    if num == 2:
        return True
    for i in range(11, num//2):
        if num%i == 0:
            return False
    return True

num1 = int(input())

if is_prime(num1):
    print("True")
else:
    print("False")