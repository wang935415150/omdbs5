#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/26
import importlib
from lib.config import settings
import traceback

class PluginManager():
    def __init__(self):
        self.mode=settings.MODE
        self.saltname=settings.SALTNAME
        self.plugin_item=settings.PLUGIN_ITEMS
        self.test=settings.TEST
        if self.mode=="SSH":
            self.hostname = settings.SSH_HOSTNAME
            self.username = settings.SSH_USERNAME
            self.password = settings.SSH_PASSWORD
            self.port = settings.SSH_PORT
    def exec_plugin(self):
        server_info={}
        for k,v in self.plugin_item.items():
            info={"status":True,"data":None,'msg':None}
            # try:
            module_path,cls_name = v.rsplit(".",maxsplit=1)
            module = importlib.import_module(module_path)
            cls =getattr(module,cls_name)
            obj = cls()
            ret = obj.process(self.exec_cmd,self.test)
            info['data']=ret
            # except Exception as e:
            #     info['status']=False
            #     info['msg']=traceback.format_exc()
            server_info[k]=info
        return server_info
    def exec_cmd(self,cmd):
        if self.mode=="ANGET":
            import subprocess
            result=subprocess.getoutput("ifconfig")
        elif self.mode=="SSH":
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            stdin, stdout, stder = ssh.exec_command("ifconfig")
            result = stdout.read()
            ssh.close()
        elif self.mode=="SALT":
            import subprocess
            result=subprocess.getoutput('salt "%s" cmd.run "%s"' %(self.saltname,cmd))
        else:
            raise Exception("请在settings中MODE选择正确的一种")
        return result