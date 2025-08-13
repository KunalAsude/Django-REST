
from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path("students/",views.studentsView),
    path("students/<int:pk>/",views.studentDetailView),

    # path('employees/',views.employees.as_view()),
    # path('employees/<int:pk>/',views.employeeDetailView.as_view())

    path('',include(router.urls))
]
