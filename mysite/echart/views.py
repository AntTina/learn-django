from django.shortcuts import render
from django.http import HttpResponse
import os
import json
# Create your views here.

def index(request):
    u1=os.popen("df|egrep '/$'|awk '{print $5}'|tr -d '%'").read()
    u2=os.popen("df|egrep '/boot$'|awk '{print $5}'|tr -d '%'").read()
    u3=os.popen("df|egrep '/yum$'|awk '{print $5}'|tr -d '%'").read()
    return render(request, 'echart/index.html', {'u1':u1 ,'u2':u2, 'u3':u3 })

def cpu(request):
    return render(request, 'echart/cpu.html')

def cpu_info(request):
    cmd = "iostat 1 2 |egrep -v [a-Z]|egrep [0-9]|tail -1"
    result = os.popen(cmd).readline().split()
    iostat = [float(f) for f in result]
    output = json.dumps(iostat)
    return HttpResponse(output)

def load(request):
    return render(request, 'echart/load.html')

def load_info(request):
    cmd = "uptime|awk -F : '{print $5}'|tr -d ','"
    result = os.popen(cmd).readline().split()
    load = [float(f) for f in result]
    output = json.dumps(load)
    return HttpResponse(output)
