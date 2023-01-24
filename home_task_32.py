# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("a = "))
b = int(input("b = "))
def pw(x, y):
    if (y == 1):
        return (x)
    if (y != 1):
        return (x * pw(x, y - 1))
pow = pw(a, b)
print(pow)
