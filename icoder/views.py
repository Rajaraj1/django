from django.http import request
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def form(request):
    a = request.GET.get('fname')
    b = request.GET.get('fpass')
    c = request.GET.get('ftext')
    d = request.GET.get('fcheck')
    dic = {'name': a,'pass':b,'text':c,'check':d}
    return render(request,'form.html',dic)
    