#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wyd"
# Date: 2017/9/27

from repository import models
def add_info(ret):
    hostname=ret['basic']['data']['hostname']
    server_obj=models.Server.objects.filter(hostname=hostname).first()

    nic_info = ret['nic']['data']
    disk_info = ret['disk']['data']
    memory_info = ret['memory']['data']
    if not server_obj:
        server_info={}
        server_info.update(ret['basic']['data'])
        server_info.update(ret['board']['data'])
        server_obj=models.Server.objects.create(**server_info)
        for i in nic_info:
            nic_dic=nic_info[i]
            models.NIC.objects.create(name=i,server_obj=server_obj,**nic_dic)
        for i in disk_info:
            disk_dic=disk_info[i]
            models.Disk.objects.create(server_obj=server_obj,**disk_dic)
        for i in memory_info:
            memory_dic=memory_info[i]
            models.Memory.objects.create(server_obj=server_obj,**memory_dic)
    else:
        nic_obj=server_obj.nic.values('name','hwaddr','netmask','ipaddrs','up')
        new_nic_info=[]
        for k,v in nic_info.items():
            v['name']=k
            new_nic_info.append(v)

        set(list(nic_obj))
        set(new_nic_info)
        # set1={1,2}
        # set2={1,2,3,4}
        #
        # print (set1 & set2)
