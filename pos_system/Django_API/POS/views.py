from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# from POS.models import Departments, Employees
# from POS.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.


# Renders html code
def index(request):
    return render(request, 'base.html')


# This is managing how data is deleted, added, etc
# @csrf_exempt
# def departmentApi(request, id=0):
#     # Converts data to JSON file
#     if request.method == 'GET':
#         departments = Departments.objects.all()
#         departments_serializer = DepartmentSerializer(departments, many=True)
#         return JsonResponse(departments_serializer.data, safe = False)
#     elif request.method == 'POST':
#         department_data = JSONParser().parse(request)
#         departments_serializer = DepartmentSerializer(data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Added Succesfully", safe = False)
#         return JsonResponse("Failed to Add", safe = False)
#     elif request.method == 'PUT':
#         department_data = JSONParser().parse(request)
#         department = Departments.objects.get(DepartmentID=department_data['DepartmentID'])
#         departments_serializer = DepartmentSerializer(department, data = department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Update Succesfully", safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method == 'DELETE':
#         department = Departments.objects.get(DepartmentID = id)
#         department.delete()
#         return JsonResponse("Deleted Succesfully", safe=False)
    