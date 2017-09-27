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
    print(ret)
    return HttpResponse("ok")