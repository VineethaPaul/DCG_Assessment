from rest_framework import serializers
from empapp.models import *
from django.contrib.auth.models import User

class EmpSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmployeeDetails
		fields = '__all__'


class DeptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Departments
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','password']
