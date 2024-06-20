fp1=open("CSEA.txt","r")
fp2=open("CSEA1.txt","w+")
if fp1:
    print("file opened")
for i in fp1:
    fp2.write(i)
    print("file is copied")
    fp2.seek(0,0)
    content=fp2.read()
    print(content)
    fp1.close()
    fp2.close()