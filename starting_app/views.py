from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, StudentForm

# Create your views here.
def index(request):
    std=Student.objects.all()
    return render(request, 'index.html', context={"students":std, "form":StudentForm()})

def get_student(request, pk):
    std=Student.objects.get(id=pk)
    return render(request, 'student.html', context={"student":std})
# for saving students data
def createStudent(request):
    if request.method == "POST":
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()
    return render(request, 'index.html', context={"students":Student.objects.all()} )


# def home(request):
    # return HttpResponse("Hello, world")

# def about(request):
#     return HttpResponse("This is about page")

# def contact(request):
#     return HttpResponse("This is contact page")
