#!/usr/bin/env python
#coding:utf-8
# license removed for brevity

import threading
import time
from Queue import Queue

class workerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put_nowait(item)

    def close(self):
        self.input_queue.put_nowait(None)
        self.input_queue.join()

    def run(self):
        while True:
            # time.sleep(3)
            item = self.input_queue.get()  # error:if replaced with self.input_queue.get_nowait()
            if item is None:
                print 'thread is closed'
                break
            print item
            self.input_queue.task_done()
        self.input_queue.task_done()
        return

wt = workerThread()
wt.start()
wt.send("hello")
wt.send("a queue test")
wt.close()