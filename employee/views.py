

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/emp_list.html', {'employees': employees})

def emp_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('emp_list')
    return render(request, 'employee/emp_form.html', {'form': form})

def emp_update(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('emp_list')
    return render(request, 'employee/emp_form.html', {'form': form})

def emp_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_list')
    return render(request, 'employee/emp_confirm_delete.html', {'employee': employee})
