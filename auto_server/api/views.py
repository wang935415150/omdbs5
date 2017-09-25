from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.

@csrf_exempt
def server(request):
    print(request.POST)
    return HttpResponse("ok")