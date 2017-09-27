from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
import json
@csrf_exempt
def server(request):
    ret=json.loads(request.body)
    print(ret["nic"])
    return HttpResponse("ok")