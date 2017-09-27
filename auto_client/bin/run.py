#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/25

import sys
import os
import requests
import json
BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)
os.environ['AUTO_CLIENT_SETTINGS']="conf.settings"
from lib.config import settings

from src.plugins import PluginManager
if __name__=="__main__":
    obj=PluginManager()
    server_dic=json.dumps(obj.exec_plugin())
    requests.post(settings.API,server_dic)
