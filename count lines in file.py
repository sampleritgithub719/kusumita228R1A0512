fp=open("count.txt","r")
words=[]
lines=0
charcount=0
for i in fp:
    charcount++;
lines+=readline()
words=i.split(" ")

print(len(words))
print(charcount)