fp=open("C.txt","w")
if fp:
    print("file is created")
    fp.write("hello cse")
    fp.writelines("hi welocme to cmrec")
    fp.close()