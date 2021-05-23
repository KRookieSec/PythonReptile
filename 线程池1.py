#coding:utf-8
#线程池
#导入模块
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
def fn(name):
    for i in range(10000):
        print(name,i)
if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f"线程{i} ")
    #等待线程池中的任务全部执行完毕，才继续执行，称为守护
    print("123")