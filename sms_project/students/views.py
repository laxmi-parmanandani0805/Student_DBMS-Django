from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Course
from .forms import StudentForm
from django.db.models import Avg,Q
from django.contrib import messages


def index(request):
    query = request.GET.get('q')

    students = Student.objects.all().order_by('roll_no')

    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(roll_no__icontains=query)
        )

    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    average_marks = Student.objects.aggregate(Avg('marks'))['marks__avg']

    context = {
        'students': students,
        'total_students': total_students,
        'total_courses': total_courses,
        'average_marks': average_marks,
        'query': query,
    }

    return render(request, 'students/index.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('index')
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {'form': form})

def delete_student(request, roll):
    student = get_object_or_404(Student, roll_no=roll)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('index')

    return render(request, 'students/delete.html', {'student': student})

def update_student(request, roll):
    student = get_object_or_404(Student, roll_no=roll)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('index')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/update.html', {'form': form, 'student': student})