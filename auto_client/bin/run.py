#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/25

import sys
import os
BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)
os.environ['AUTO_CLIENT_SETTINGS']="conf.settings"

from src import script
if __name__=="__main__":
    obj=script.start()
