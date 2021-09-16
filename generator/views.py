from django.shortcuts import render
from django.http import HttpResponse
import os

cwd = os.chdir("C:\\Users\ADMIN\mynewweb")

# Create your views here.
def ho(request):
    return HttpResponse('HELLO WORLD')

def home(request):
    return render(request,'generator\home.html', {'100mm' : 150})

def firehydrant(request):
    dia = int(request.GET.get('DIA'))
    hpm = request.GET.get('hpm')
    inlet = request.GET.get('INLET')
    lines = request.GET.get('LINES')
    rmt = request.GET.get('RMT')
    extra_percentage = request.GET.get('extra_percentage')


    return render(request,'generator\irehydrant.html', {'dia' : dia , 'hpm' : hpm , 'inlet' : inlet , 'lines' : lines , 'rmt' : rmt , 'extra_percentage' : extra_percentage })

def sprinkler(request):
    return render(request,'generator\sprinkler.html', {'100mm' : 150})

def boq(request):
    return render(request,r'generator/boq.html', {'100mm' : 150})

