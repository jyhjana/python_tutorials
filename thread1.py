#!/usr/bin/env python
#coding:utf-8
# license removed for brevity
import threading

def func1(num):
    for i in range(num):
        #threading.currentThread()
        print 'I am %s.num:%s' % (threading.currentThread().getName(), i)


def main(thread_num):
    thread_list = []
    for i in range(thread_num):
        thread_list.append(threading.Thread(target=func1, args=(3,)))
    for a in thread_list:
        # a.setDaemon(True)这个setDaemon默认为False 非守护线程
        # 表示主线程等所有子线程结束后，在结束
        # 设置为True的话 表示是个守护线程 子线程就会随着主线程的结束而结束
        # 听说服务监控工具生成的心跳线程 就是用的守护线程
        a.start()

    for a in thread_list:
        a.join()  # 表示等待直到线程运行完毕


main(3)