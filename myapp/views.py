from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
import pyexecutor

def index(request):
    # Load our 
    return render(request, 'enterpythoncode.html')

def submit(request):
    try:
        script_code = request.POST['script_code']
        script_name = request.POST['script_name']
    except (KeyError):
        return render(request, 'templates/error.html', {
            'error_message': "Some error happened",
        })
    else:
        file_name = pyexecutor.create_script_file(script_name, script_code)
        return HttpResponse(pyexecutor.execute_file(file_name))
