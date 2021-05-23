#coding:utf-8
#多线程的第二种写法
import threading 
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        for i in range(500):
            print(self,i)
if __name__ == '__main__':
    t1 = MyThread("子线程1 ")
    t1.start()
    for i in range(500):
        print("主线程 ",i)
    t2 = MyThread("子线程2 ")
    t2.start()