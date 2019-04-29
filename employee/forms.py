from django import forms  
from employee.models import Employee 
from employee.models import Datetest
from employee.models import Cat 
from django.contrib.admin import widgets
from django.forms.widgets import *
import datetime
class EmployeeForm(forms.ModelForm):
    #CHOICES = (('Ali', 'Ali'),('Azad', 'Azad'),('Tanim', 'Tanim'),('zahid', 'zahid'),)
    eid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'id'}),required=True,max_length=100)
    ename=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}),required=True,max_length=100)    
    #ename= forms.CharField(widget=forms.Select(attrs={'class':'selectpicker','data-style':'btn-primary','id':'sel'}, choices=CHOICES))
    eemail = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),required=True,max_length=100)
    econtact=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'contact'}),required=True,max_length=100)
    ecat= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Cat.objects.order_by('caty')),queryset=Cat.objects.order_by('caty'))    
    #ecat= forms.ModelChoiceField(widget=forms.Select(attrs={'data-style':'btn-primary','id':'sel'}, choices=Employee.objects.order_by('ename')),queryset=Employee.objects.order_by('ename'))    
    
    class Meta:  
        model = Employee  
        fields = "__all__"
class CatForm(forms.ModelForm):
    class Meta:  
        model = Cat  
        fields = "__all__"
class DatetestForm(forms.ModelForm):
    #tdate=forms.DateField()
    #tdate=forms.DateField(widget = forms.SelectDateWidget)
    #cur_year = datetime.datetime.today().year
    #year_range = tuple([i for i in range(cur_year - 2, cur_year + 2)])
    #tdate = forms.DateField(initial=datetime.date.today() ,widget=forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}))
    tdate=forms.DateField(initial=datetime.date.today(), widget=forms.DateInput(attrs={'id': 'datespan'}))
    class Meta:
        model=Datetest
        fields = "__all__"



#choices first values, second name
#for selecting a single field
#Employees.objects.only('eng_name')

#for selecting more then one field
#Employees.objects.values_list('eng_name', flat=True)
#Employees.objects.values_list('eng_name', 'rank')



#Giving Limitations in django form datefield
#import datetime
#from django import forms
#class HistDateForm(forms.Form):
#   cur_year = datetime.datetime.today().year
#  year_range = tuple([i for i in range(cur_year - 2, cur_year + 2)])
#    hist_date = forms.DateField(initial=datetime.date.today() - datetime.timedelta(days=7),widget=forms.SelectDateWidget(years=year_range))


#stylize the selectdatewidget field with css
#form
#tdate = forms.DateField(initial=datetime.date.today() ,widget=forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}))
#'calss' : 'form-control classname'   here 'form-control' is important
#css
#.snps-inline-select {
#    width: auto;
#    display: inline-block;
#}