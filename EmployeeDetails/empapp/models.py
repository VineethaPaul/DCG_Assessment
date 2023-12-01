from django.db import models


class Departments(models.Model):
	dept_id =  models.AutoField(primary_key=True)
	dept_name = models.CharField(max_length=200,blank=True, null=True)
	
class EmployeeDetails(models.Model):
	emp_id = models.AutoField(primary_key=True)
	emp_name = models.CharField(max_length=150,blank=True, null=True)
	emp_salary = models.CharField(max_length=150,blank=True, null=True)
	dept_id = models.ForeignKey(Departments,on_delete=models.CASCADE)
	

