from django import forms  
from employee.models import Employee 
from employee.models import Cat 
class EmployeeForm(forms.ModelForm):
    #CHOICES = (('Ali', 'Ali'),('Azad', 'Azad'),('Tanim', 'Tanim'),('zahid', 'zahid'),)
    eid=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'id'}),required=True,max_length=100)
    ename=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}),required=True,max_length=100)    
    #ename= forms.CharField(widget=forms.Select(attrs={'class':'selectpicker','data-style':'btn-primary','id':'sel'}, choices=CHOICES))
    eemail = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),required=True,max_length=100)
    econtact=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'contact'}),required=True,max_length=100)
    ecat= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'selectpicker','data-style':'btn-primary','id':'sel'}, choices=Cat.objects.all()),queryset=Cat.objects.all())    
    class Meta:  
        model = Employee  
        fields = "__all__"
class CatForm(forms.ModelForm):
    class Meta:  
        model = Cat  
        fields = "__all__"



#choices first values, second name