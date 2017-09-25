#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/25

import subprocess
import requests
result = subprocess.getoutput("ipconfig")
print(result)
result=result[359:372]
api="http://127.0.0.1:8000/api/server.html"
requests.post(url=api,data={"ip":result})