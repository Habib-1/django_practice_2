from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    d={"name":"Habib", "age" :24, 'courses':
       [
           {
             'id':1,
             'name':"React-js" ,
             'fee':2500
           },
           {
             'id':2,
             'name':"Python",
             'fee':6000 
           },
           {
             'id':3,
             'name':"Django",
             'fee':5000  
           },
           {
             'id':4,
             'name':"MySQL",
             'fee': 3000 
           },
       ]
       }
    return render(request,'home.html',d)
