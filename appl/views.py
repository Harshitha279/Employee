from django.shortcuts import render, redirect
from .models import Employee
from django.db import IntegrityError

def display(request):
    if request.method == "POST":
        empno = request.POST.get('empno')
        empname = request.POST.get('empname')

        # Check if empno already exists
        if Employee.objects.filter(empno=empno).exists():
            error = f"Employee with number {empno} already exists."
            return render(request, 'input.html', {'error': error})

        # Save if not exists
        try:
            Employee.objects.create(empno=empno, empname=empname)
        except IntegrityError:
            error = "An error occurred while saving the employee."
            return render(request, 'input.html', {'error': error})

        return render(request, 'display.html', {'empno': empno, 'empname': empname})

    return redirect('input_form')

def input_form(request):
    return render(request, 'input.html')
