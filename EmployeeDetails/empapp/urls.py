from django.urls import path
from .views import *

urlpatterns = [
	path('signup/', SignUpAPI.as_view(), name='user_signup'),
    path('login/', LoginAPI.as_view(), name='user_login'),
    path('emp_details/',EmpDetailsAPI.as_view(),name="EmpDetails"),
    path('emp_details/<int:pk>/',EmpDetailsAPI.as_view(),name="EmpDetails"),
    path('department_details/',DepartmentDetailsAPI.as_view(),name="DepartmentDetails"),
    path('department_details/<int:pk>/',DepartmentDetailsAPI.as_view(),name="DepartmentDetails"),
]