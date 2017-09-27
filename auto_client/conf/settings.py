#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/25

import sys
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
PLUGIN_ITEMS = {
    "nic":"src.plugins.nic.Nic",
    "disk":"src.plugins.disk.Disk",
}

API="http://127.0.0.1:8000/api/server.html"

SSH_HOSTNAME='192.168.16.159'
SSH_USERNAME='root'
SSH_PORT=22
SSH_PASSWORD='1234'

SALTNAME='*'

TEST=True

MODE='ANGET' #只能写ANGET/SSH/SALT