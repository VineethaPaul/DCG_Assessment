from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# User Signup API
class SignUpAPI(APIView):
    def post(self, request):
        email 		=	request.data.get('email')
        password 	=	request.data.get('password')
        
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user 		= 	User.objects.create_user(username=email, email=email, password=password)
        serializer 	= 	UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# User Login API
class LoginAPI(APIView):
    def post(self, request):
        email 		= 	request.data.get('email')
        password 	= 	request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user 		= 	User.objects.filter(email__iexact=email).first()

        if user and user.check_password(password):
            refresh = 	RefreshToken.for_user(user)
            return Response({'access_token': str(refresh.access_token)}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Employee Table CRUD API
class EmpDetailsAPI(APIView):
	# permission_classes = [IsAuthenticated]

	def get_object(self, pk):
		try:
			data = EmployeeDetails.objects.get(emp_id=pk)
			return data
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
	def get(self, request):
		empModel = EmployeeDetails.objects.all()
		serializer = EmpSerializer(empModel,many=True)
		return Response(serializer.data)

	def post(self, request):
		print(request.data,'--------------------------------')
		serializer = EmpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

	def put(self, request,pk):
		updateData = self.get_object(pk)
		serializer = EmpSerializer(updateData,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def delete(self, request,pk):
		try:
			deleteData = self.get_object(pk)
			deleteData.delete()
			return Response('Data Deleted',status=status.HTTP_204_NO_CONTENT)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	
# Department Table CRUD API
class DepartmentDetailsAPI(APIView):
	serializer_class 	= DeptSerializer
	permission_classes 	= 	[IsAuthenticated]

	def get_object(self, pk):
		try:
			data = Departments.objects.get(dept_id=pk)
			return data
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request):
		# print('get','pkpkpkpkpkp')
		# getDetails = self.get_object(pk)
		# serializer = DeptSerializer(getDetails)

		empModel = Departments.objects.all()
		serializer = DeptSerializer(empModel,many=True)
		return Response(serializer.data)

	def post(self, request):
		# print(request.data,'--------------------------------')
		serializer = DeptSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

	def put(self, request,pk):
		# print('puttttttttttttt',pk)
		updateData = self.get_object(pk)
		serializer = DeptSerializer(updateData,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request,pk):
		# print(pk,'-----pkpkpkpk================================')
		try:
			deleteData = self.get_object(pk)
			deleteData.delete()
			return Response('Data Deleted',status=status.HTTP_204_NO_CONTENT)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	
	
