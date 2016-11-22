#!/usr/bin/env python3
# coding=utf-8

"""
module/program document
"""

from queue import Queue
from threading import Thread


class producer(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        self.count = 5
        while self.count > 0:
            if self.count == 1:
                self.count -= 1
                self.q.put(2)
            else:
                self.count -= 1
                self.q.put(1)


class consumer(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            data = self.q.get()
            if data == 2:
                print("stop because data=", data)
                self.q.task_done()
                break
            else:
                print("data is good,data=", data)
                self.q.task_done()


def main():
    qq = Queue()
    p = producer(qq)
    c = consumer(qq)
    p.setDaemon(True)
    c.setDaemon(True)
    p.start()
    c.start()
    qq.join()
    print("queue is complete")


if __name__ == '__main__':
    main()