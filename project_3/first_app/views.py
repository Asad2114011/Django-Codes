from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={'author':'asad','age':23,'lst':['python','is','best'],'val' :'','birthday':datetime.datetime.now(),'courses':[
        {
            'id':1,
            'name':'django',
            'fees':2000,
        },
        {
            'id':2,
            'name':'algorithm',
            'fees':3000,
        },
        {
            'id':3,
            'name':'oop',
            'fees':9000,
        },
    ]}
    return render(request,'home.html',d)