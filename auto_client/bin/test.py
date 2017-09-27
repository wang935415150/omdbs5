#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/27
import time
from concurrent.futures import ThreadPoolExecutor#这就是线程池
from concurrent.futures import ProcessPoolExecutor#这就是进程池
def task(arg1,arg2):
    print(arg1,arg2)
    time.sleep(1)


pool = ThreadPoolExecutor(10)

for i in range(100):
    pool.submit(task,i,i)