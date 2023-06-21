import json
from django.shortcuts import render,redirect
from employee.serializer import EmpSerializer
from .models import Emp
from django.db import connection
from django.db import connections

# Create your views here.


def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email_=request.POST['email']
        doj=request.POST['doj']
        location=request.POST['select']
        insert_data = f"INSERT INTO employee (name, email, doj, location) VALUES ('{name}', '{email_}', '{doj}', '{location}')"
        with connection.cursor() as cursor:
            cursor.execute(insert_data)
        return redirect('/alldata')
    return render(request,'index.html')

def alldata(request):
    contex={}
    contex['data']=Emp.objects.raw("select * from employee")
    data = EmpSerializer(Emp.objects.all(), many=True).data
    print(json.dumps(data))
    return render(request,'alldata.html',contex) 

def delete(request,pid):
    delete_data = f"DELETE FROM employee WHERE id = {pid}"
    with connection.cursor() as cursor:
        cursor.execute(delete_data)
    return redirect('/alldata')

def update(request,pid):
    if request.method == "POST":
        name=request.POST['name']
        email_=request.POST['email']
        doj=request.POST['doj'] 
        location=request.POST['select']
        update_data = f"UPDATE employee SET name = '{name}', email = '{email_}', doj = '{doj}', location = '{location}' WHERE id = {pid}"
        with connection.cursor() as cursor:
            cursor.execute(update_data)
        return redirect('/alldata')
    data=Emp.objects.get(id=pid)
    content={'data':data}        
    return render(request,'update.html',content)

def mumbai(request):
    data=Emp.objects.raw("select * from employee where location='Mumbai'")
    content={'data':data}
    return render(request,'alldata.html',content)

def delhi(request):
    data=Emp.objects.raw("select * from employee where location='Delhi'")
    content={'data':data}
    return render(request,'alldata.html',content)

def pune(request):
    data=Emp.objects.raw("select * from employee where location='Pune'")
    content={'data':data}
    return render(request,'alldata.html',content)

def bangalore(request):
    data=Emp.objects.raw("select * from employee where location='Bangalore'")
    content={'data':data}
    return render(request,'alldata.html',content)

def refresh(request):
    data=Emp.objects.raw("select * from employee")
    content={'data':data}
    return render (request,'alldata.html',content)

