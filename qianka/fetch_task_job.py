#!/usr/bin/python
# -*-coding:utf-8-*-


import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import httplib

import time

import taskrunner
from db import disciple

if __name__ == '__main__':
    while 1:
        for data in disciple.fetch_by_master('33005806'):
            taskrunner.complete_task(data)
        time.sleep(2)
