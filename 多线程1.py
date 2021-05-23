#coding:utf-8
#多线程的第一种写法
from threading import Thread   #线程类
def func(name):
    for i in range(500):
        print(name,i)
if __name__ == '__main__':
    t1 = Thread(target=func,args=("线程1",))     #传递参数到线程中，参数必须是元组
    t1.start()
    t2 = Thread(target=func,args=("线程2",))
    t2.start()
    #主线程
    for i in range(500):
        print("main ",i)