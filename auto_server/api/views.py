from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from repository import models
# Create your views here.
import json
@csrf_exempt
def server(request):
    ret=request.body
    ret=json.loads(ret.decode('utf-8'))
    hostname=ret['basic']['data']['hostname']
    server_obj=models.Server.objects.filter(hostname=hostname).first()
    if not server_obj:
        server_info={}
        server_info.update(ret['basic']['data'])
        server_info.update(ret['board']['data'])
        server_obj=models.Server.objects.create(**server_info)
    nic_info=ret['nic']['data']
    for i in nic_info:
        nic_dic=nic_info[i]
        models.NIC.objects.create(name=i,server_obj=server_obj,**nic_dic)
    disk_info=ret['disk']['data']
    for i in disk_info:
        disk_dic=disk_info[i]
        models.Disk.objects.create(server_obj=server_obj,**disk_dic)
    memory_info=ret['memory']['data']
    for i in memory_info:
        memory_dic=memory_info[i]
        models.Memory.objects.create(server_obj=server_obj,**memory_dic)
    return HttpResponse("ok")