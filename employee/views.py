from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee 
from django.db.models import Q 
from django.contrib import messages
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import timedelta
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/show')
            except:
                pass  
    else:
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})

def show(request):  
     #date2 = '2019-03-10 09:56:28.067'
    employees = Employee.objects.all() 
    field_name = 'created_at'
    obj = Employee.objects.first()
    field_value = getattr(obj, field_name)
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    date1 = str(datetime.datetime.now())
    date2= str(field_value)
    diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2[0:25], datetimeFormat)
    context={
        'diff': diff,
        'employees':employees
    }
    return render(request,"show.html",context)

def edit(request, id):  
    employee = Employee.objects.get(id=id) 
    form = EmployeeForm()
    context={
        'form': form,
        'employee':employee
    } 
    return render(request,'edit.html', context)

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)
    context={
        'employee':employee
    }
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html',context)

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")
def search(request):
    if request.method=='POST':
        srch=request.POST['srh']

        if srch:
            match=Employee.objects.filter(Q(ename__icontains=srch) |
                                          Q(eemail__icontains=srch)
                                        )
            if match:
                return render(request, 'search.html', {'sr':match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')
