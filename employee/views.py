from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee 
from django.db.models import Q 
from django.contrib import messages
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
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
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})

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
