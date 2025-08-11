from django.shortcuts import render
from django.http import HttpResponse


def students(req):
    students = [
        {'id':1, 'name':'demo test','age':24}
    ]
    return HttpResponse(students)
