from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.forms import DatetestForm
from employee.models import Employee 
from employee.models import Datetest
from django.db.models import Q 
from django.contrib import messages
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import date
from datetime import timedelta
from django import template
register = template.Library()
@register.filter
def div( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value / arg
    except: pass
    return ''

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
    
def sorting(request):
    employees = Employee.objects.order_by('created_at')
    context={
        'employeesd':employees
    }
    return render(request,"show.html",context)

def show(request):  
     #date2 = '2019-03-10 09:56:28.067'
    employees = Employee.objects.order_by('created_at').reverse()   #created_at desc order  #reverse() for implied the Asc
    datetest1 = Datetest.objects.filter(tdate__gte=datetime.date.today())    
    datetest2 = Datetest.objects.filter(tdate__lte=datetime.date.today())
    #employees=Employee.objects.filter(created_at__lte=datetime.datetime.today())
    #employees=Employee.objects.filter(created_at__minute__gte=datetime.datetime.today().minute)
    #employees = Employee.objects.exclude(created_at__gt=datetime.datetime(2019, 4, 20,00,00,00))
    #field_name = 'created_at'
    #obj = Employee.objects.first()
    #field_value = getattr(obj, field_name)
    #datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    #date1 = datetime.datetime.now()
    #date2= str(field_value)
    #diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2[0:25], datetimeFormat)
    date1=datetime.datetime.now()
    date2=datetime.timedelta(minutes=1)
    context={
        'date1': date1,
        'date2':date2,
        'employees':employees,
        'datetest1':datetest1,
        'datetest2':datetest2
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

def datetest(request):
    if request.method == "POST":  
        form = DatetestForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                return redirect('/show')
            except:
                pass  
    else:
        form = DatetestForm()  
    return render(request,'datetesting.html',{'form':form})
