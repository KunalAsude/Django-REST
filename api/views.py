from django.shortcuts import render ,get_object_or_404
from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins,viewsets


@api_view(['GET', 'POST'])
def studentsView(req):
    if req.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(req, pk):
    student = Student.objects.get(pk=pk)
    if req.method == 'GET':
        try:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif req.method == 'PUT':
        serializer = StudentSerializer(student, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class employees(APIView):
#     def get(self, req):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, req):
#         serializer = EmployeeSerializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class employeeDetailView(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,req,pk):
        employee = self.get_object(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,req,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# mixins
# class employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,req):
#         return self.list(req)

#     def post(self,req):
#         return self.create(req)        
    
# class employeeDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset =Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,req,pk):
#         return self.retrieve(req,pk)
    
#     def put(self,req,pk):
#         return self.update(req,pk)
#     def delete(self,req,pk):
#         return self.destroy(req,pk)

# Generics 
# class employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class employeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field ='pk'

#viewSet
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,req):
#         queryset = Employee.objects.all()
#         serializer=EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data)
#     def create(self,req):
#         serializer=EmployeeSerializer(data =req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
#     def retrieve(self,req,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def update(self,req,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee,data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else: 
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,req,pk=None):
#         employee = get_object_or_404(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#viewSet.modelViewset

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer