fp1=open("CSEA.txt","r")
if fp1:
       print("file opened")
       fp1.seek(5, 0)
       for i in fp1:
          print(i)
fp1.close()
'''content=fp1.readline()
   print(content)
   content=fp1.readline()
   print(content)'''