from django.urls import path

from EmployeeApp import views

urlpatterns = [
    path('', views.view_emp, name="view"),
    path('del/<int:id>/', views.del_emp, name='del')
]
