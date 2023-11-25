from django.shortcuts import render, redirect

from EmployeeApp.models import Employee


# Create your views here.
def view_emp(request):
    data = Employee.objects.all()
    return render(request, 'ViewEmp.html', {"data": data})


def del_emp(request, id):
    if request.method == "POST":
        del1 = Employee.objects.get(id=id)
        del1.delete()
        return redirect('view')
    return render(request, 'ViewEmp.html')
