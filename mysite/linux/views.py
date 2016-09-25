from django.shortcuts import render
from os import popen

# Create your views here.


def index_cmd(request, command):
    results = ''.join(popen(command).readlines())
    return render(request, 'linux/index.html', {'results':results, 'cmd':command})

def index_form(request):
	cmd = request.POST['command']
	results = ''.join(popen(cmd).readlines())    
	return render(request, 'linux/index.html', {'results':results, 'cmd':cmd})

def index(request):
    return render(request, 'linux/index.html', {'results':'Display Linux System Information'})
