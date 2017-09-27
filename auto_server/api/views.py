from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from repository import models
from api import mylib
# Create your views here.
import json
@csrf_exempt
def server(request):
    ret=request.body
    ret=json.loads(ret.decode('utf-8'))
    mylib.add_info(ret)
    return HttpResponse("ok")