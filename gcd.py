def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

if a > b:
    temp = a
    a = b
    b = temp

print('GCD of', a, 'and', b, 'is:', gcd(a, b))
