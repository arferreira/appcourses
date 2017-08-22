from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    template_name = 'courses/course_list.html'
    return render(request, template_name, context)
'''
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course,
    }
    template_name = 'courses/course_detail.html'
    return render(request, template_name, context)
'''

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    form = ContactCourse()
    context = {
        'course': course,
        'form': form,
    }
    template_name = 'courses/course_detail.html'
    return render(request, template_name, context)
