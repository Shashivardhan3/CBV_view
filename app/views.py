from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
#rendering of string by fbv
def fbv_string(request):
    return HttpResponse('this is fbv string')

#rendering of string by cbv
class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is cbv string')

#rendering of htmlpage by fbv

def fbv_page(request):
    return render(request,'fbv_page.html')


#rendering of htmlpage by cbv

class cbv_page(View):
    def get(self,request):
        return render (request,'cbv_page.html')
    

#insertion of data by fbv

def insert_by_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted')
    return render(request,'insert_by_fbv.html',d)


#insertion of data by CBv

class insert_by_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_by_cbv.html',d)
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted')