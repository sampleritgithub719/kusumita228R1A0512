i = int(input("Enter the starting number: "))
u = int(input("Enter the ending number: "))

print("Prime numbers between", i, "and", u, "are:")

for num in range(i, u + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
i=int(input())
u=int(input())
print("Prime numbers between",i,"and",u,"are:")
for num in range(i,u+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
            else:
                print(num)

