from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required


def register_student(request):
    if request.method == 'POST':
        student = Student(
            student_name=request.POST['student_name'],
            email=request.POST['email'],
            age=request.POST['age'],
            mobile_number=request.POST['mobile_number'],
            course=request.POST['course'],
            profile_image=request.FILES['profile_image']
        )
        student.save()
        return redirect('student_list')

    return render(request, 'students/register.html')

def student_list(request):
    students = Student.objects.all()
    if request.method == 'GET':
        return render(request, 'students/students_list.html', {
        'students': students
    })

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html',
                  {'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete_student.html',
                  {'student': student})

@login_required(login_url='login')
def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Student.objects.values('course').distinct().count()

    recent_students = Student.objects.order_by('-created_date')[:5]

    return render(request, 'students/dashboard.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'recent_students': recent_students,
    })