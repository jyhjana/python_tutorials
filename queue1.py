#!/usr/bin/env python

'''
Created on Apr 25, 2012

@author: stedy
'''
# coding=cp936
from random import randint
from time import sleep, ctime
from Queue import Queue
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print'stating', self.name, 'at', ctime()
        self.func(*self.args)


def writeQ(queue):
    i = randint(1, 100)
    print 'producing object for Q...', queue.put(i, 1)


def readQ(queue):
    if queue.empty() == False:
        val = queue.get(1)
        print 'value from Q', val
    else:
        print "no value,wait a moment"
        sleep(1)


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(1, 3))


funcs = [reader, writer]
nfuncs = range(len(funcs))


def main():
    nloops = 99
    q = Queue(100)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
    print 'all Done'


if __name__ == '__main__':
    main()