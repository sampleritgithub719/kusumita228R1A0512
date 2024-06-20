import threading
def square(n):
    print(n*n)
def cube(m):
    print(m*m*m)
t1=threading.Thread(target=square,args=(3,))
t2=threading.Thread(target=cube,args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()