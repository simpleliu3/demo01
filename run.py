# coding=utf-8

import threading
from httprunner.api import HttpRunner


class myThreads(threading.Thread):
    def __init__(self, threadName):
        super(myThreads, self).__init__()
        self.threadName = threadName

    def run(self):
        runner = HttpRunner()
        runner.run(self.threadName)


items = ["testcases/t1.yml", "testcases/t2.yml"]
threads = []
for i in items:
    thread = myThreads(i)
    thread.start()
    threads.append(thread)

for j in threads:
    j.join()

# runner = HttpRunner()
# runner.run('testsuites/t1.yml')
