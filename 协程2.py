#coding:utf-8
#编写协程程序
#导入协程模块
import asyncio
import time

async def func1():      #def前加async，函数就变成了协程函数
    print("你好，我是甲！")
    #time.sleep(1)       #当程序出现同步操作时，异步就中断了
    await asyncio.sleep(1)    #异步操作代码，加上await，会将当前函数挂起切换到其他函数
    print("你好，我是甲！")

async def func2():
    print("你好，我是乙！")
    #time.sleep(2)
    await asyncio.sleep(2)
    print("你好，我是乙！")

async def func3():
    print("你好，我是丙！")
    #time.sleep(3)
    await asyncio.sleep(3)
    print("你好，我是丙！")

#真正编写程序时写协程的写法,写一个协程的主函数，在程序主函数中调用协程主函数
async def main():
    #在协程主函数中同时将协程函数跑起来
    #第一种写法
    '''
    f1 = func1()
    await f1    #一般await挂起操作放在协程对象前面
    '''
    #第二种写法（推荐）
    #将协程函数放入一个列表
    tasks = [ 
        #python3.8以后的版本需要将协程对象包装成task对象，如下
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    #将列表放入协程挂起操作中
    await asyncio.wait(tasks)

if __name__ == '__main__':
    '''
    #调用函数
    f1 = func1()      #此时函数执行就成了协程函数，得到的是一个协程变量
    f2 = func2()
    f3 = func3()
    #将函数放进一个列表
    tasks = [
        f1,f2,f3
    ]
    #启动前记录一次时间
    t1 = time.time()
    #一次性启动多个任务（协程）
    asyncio.run(asyncio.wait(tasks))
    #启动后记录一次时间
    t2 = time.time()
    #输出程序执行的时间
    print(t2 - t1)
    '''
    #启动前记录一次时间
    t1 = time.time()
    #调用协程主函数，通过协程一次性启动多个任务
    asyncio.run(main())
    #启动后记录一次时间
    t2 = time.time()
    #输出程序执行的时间
    print(t2 - t1)