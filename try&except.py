'''1.try
2.except(catch)
3.else:
4.raise(throw)
5.assert(throws)'''
#zero division
'''try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except:
    print("cannot divide by zero")'''
#name exception
'''try:
    a = int(input())
    b = int(input())
    c = a / b
    print(c)
except Exception:
       print("b value is not mentioned")
       print("After exception")'''
#value error
'''try:
     a=int(input())
     print(a)
except:
     print("value error")'''
#index error
'''try:
    a=[1,2,3,4]
    print(a[6])
except:
    print("index error")'''
#key error
'''
try:
    d={"cse":"5","ece":"4"}
    print(key["it"])
except:
    print("key error")'''

#file error
try:
    fp=open("kusu.txt","r")
except:
    print("file not found")





