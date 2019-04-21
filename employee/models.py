from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    ecat = models.CharField(max_length=30, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)  
    class Meta:  
        db_table = "employee"  
    def __str__(self):
        return self.ename
class Cat(models.Model):
    caty=models.CharField(max_length=50)
    class Meta:  
        db_table = "cat"  
    def __str__(self):
        return self.caty