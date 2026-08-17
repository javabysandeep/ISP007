from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

# Create your views here.

#READ - list all students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

# create - add a new student
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})


# update - edit an existing student
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student.html', {'form': form, 'student': student})


# delete - remove a student
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete_student.html', {'student': student})

# read - view student details
def read_student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/read_student.html', {'student': student})
