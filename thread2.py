#!/usr/bin/env python
# coding:utf-8
import threading


class MyThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        for i in range(self.num):
            print'I am %s.num:%s' % (self.getName(), i)


for i in range(3):
    t = MyThread(3)
    t.start()
    t.join()