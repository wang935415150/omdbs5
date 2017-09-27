#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/26
import os
import importlib
from . import global_settings
class Settings(object):
    '''
    global_settings 配置获取
    settings.py 配置获取
    '''
    def __init__(self):
        for item in dir(global_settings):
            if item.upper():
                k=item
                v=getattr(global_settings,item)
                setattr(self,k,v)
        settings_path=os.environ.get('AUTO_CLIENT_SETTINGS')
        md_settings=importlib.import_module(settings_path)
        for item in dir(md_settings):
            if item.upper():
                k=item
                v=getattr(md_settings,item)
                setattr(self,k,v)
settings=Settings()
