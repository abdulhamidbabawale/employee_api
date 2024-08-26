from django.urls import path
from . import views

urlpatterns = [

    path('employees', views.EmployeeListCreateView.as_view(), name='employee_list_create'),  # Handles GET and POST without ID
    path('employees/<int:id>', views.EmployeeDetailView.as_view(), name='employee_detail'),  # Handles GET, PUT, DELETE with ID

]
