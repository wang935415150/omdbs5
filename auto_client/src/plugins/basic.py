#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/25


class Basic(object):

    @classmethod
    def initial(cls):
        return cls()

    def process(self,cmd_func,test):
        if test:
            output = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c1.com'
            }
        else:
            output = {
                'os_platform': cmd_func("uname").strip(),
                'os_version': cmd_func("cat /etc/issue").strip().split('\n')[0],
                'hostname': cmd_func("hostname").strip(),
            }
        return output

