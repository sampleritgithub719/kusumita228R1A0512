n=int(input())
a=0
b=1
c=0
if n<=0:
    print("Enter positive numbers")
elif n==1:
    print(a)
else:
    print("Fibonacci series")
    print(a)
    print(b)
    while(c<n):
        c=a+b
        print(c, " ")
        a=b
        b=c