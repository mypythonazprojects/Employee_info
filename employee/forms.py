from django import forms  
from employee.models import Employee  
class EmployeeForm(forms.ModelForm):
    eid=  forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'id'}),required=True,max_length=100)
    ename=  forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'name'}),required=True,max_length=100)
    eemail = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),required=True,max_length=100)
    econtact=  forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'contact'}),required=True,max_length=100)
    class Meta:  
        model = Employee  
        fields = "__all__"