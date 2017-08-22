from django.shortcuts import render
from .models import Course

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    template_name = 'courses/course_list.html'
    return render(request, template_name, context)

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course,
    }
    template_name = 'courses/course_detail.html'
    return render(request, template_name, context)
