from django.shortcuts import render,redirect

from django.http import HttpResponse

from .forms import StudentForm

from .models import Student

# Create your views here.


def Home(request):
  form=StudentForm
  students=Student.objects.all()
  context={
    'form':form,
    'students':students
  }
  return render(request,"dashboard.html",context)

def add(request):
  form=StudentForm(request.POST)
  form.save()
  return redirect('/')

def delete(request,id):
  student=Student.objects.get(id=id)
  student.delete()
  return redirect('/')