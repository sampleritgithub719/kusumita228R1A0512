def palindrome(str):
    for i in range(0,len(str)):
        if(str[i]!=str[len(str)-i-1]):
            return False
        return True
    str=   1input("enter str")
    if(palindrome(str)==True):
        print("palindrome")
    else:
        print("not a palindrome")