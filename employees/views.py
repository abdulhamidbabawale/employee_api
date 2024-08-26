from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employees.models import Employees
from rest_framework import status
from .serializers import EmployeeSerializer
from rest_framework.views import APIView


class EmployeeListCreateView(APIView):
    """Handles GET for all employees and POST for creating a new employee."""

    def get(self, request):
        """Retrieve all employees."""
        datas = Employees.objects.all()
        serializer = EmployeeSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new employee."""
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    """Handles GET, PUT, and DELETE for a specific employee by ID."""

    def get(self, request, id):
        """Retrieve a specific employee by ID."""
        try:
            employee = Employees.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employees.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        """Update a specific employee by ID."""
        try:
            employee = Employees.objects.get(id=id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employees.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        """Delete a specific employee by ID."""
        try:
            employee = Employees.objects.get(id=id)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Employees.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)



















# @api_view(['GET'])
# def getdata(request):
#     boy={'name':'hamid','age':30}
#     return Response(boy)
@api_view(['GET'])
def getdatas(request):
    datas = Employees.objects.all()
    serializer= EmployeeSerializer(datas,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata(request,id=None):
    try:
         datas = Employees.objects.get(id=id)
         serializer= EmployeeSerializer(datas)
         return Response(serializer.data)
    except Employees.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    # return Response(serializer.data)

# @api_view(['POST'])
# def add_data(request):
#     serializer=EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['POST'])
def add_data(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 Created
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 Bad Request

@api_view(['POST','GET'])
def new_data(request, id=None):
    if request.method == 'POST':
        return add_data(request)
    elif request.method == 'GET':
        if id is None:
            # Handle retrieval of a specific employee by id
           return getdatas(request)
        elif id is not None:
           return getdata(request,id)


# @api_view(['POST'])
# def delete_data(request,id=None):
#     Employees.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
