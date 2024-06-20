import threading
def demo(n):
    print("thread",n);
t1=threading.Thread(target=demo,args=(10,))
t1.start()