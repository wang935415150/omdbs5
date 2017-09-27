#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/26
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.16.159", port=22, username="root", password="1234")
stdin, stdout, stder = ssh.exec_command("ifconfig")
result = stdout.read()
ssh.close()
print(result)
