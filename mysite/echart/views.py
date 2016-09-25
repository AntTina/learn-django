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
    cmd = "iostat 1 2 |egrep -v [a-Z]|egrep [0-9]|tail -1"
    result = os.popen(cmd).readline().split()
    num = [float(f) for f in result]
    return render(request, 'echart/cpu.html', {'list':num })

def cpu_info(request):
    cmd = "iostat 1 2 |egrep -v [a-Z]|egrep [0-9]|tail -1"
    result = os.popen(cmd).readline().split()
    num = [float(f) for f in result]
    output = json.dumps(num)
    return HttpResponse(output)
