#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/27
from concurrent.futures import ThreadPoolExecutor
from src.plugins import PluginManager
import requests
from lib.config import settings
class BaesClient(object):
    def __init__(self):
        self.api=settings.API
    def post_server_info(self,server_dic):
        response=requests.post(url=self.api,json=server_dic)
    def exec(self):
        raise NotImplementedError("请继承后实现exec方法")


class AgentClient(BaesClient):
    def exec(self):
        obj=PluginManager()
        server_dic=obj.exec_plugin()
        self.post_server_info(server_dic)

class SaltSshClient(BaesClient):
    def tesk(self,host):
        obj = PluginManager(host)
        server_dic = obj.exec_plugin()
        self.post_server_info(server_dic)
    def get_host_list(self):
        return ['c1.com','c2.com']
    def exec(self):
        pool=ThreadPoolExecutor(10)
        host_list=self.get_host_list()
        for host in host_list:
            pool.submit(self.tesk,host)
