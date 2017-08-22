from django.contrib import admin
from .models import Course



class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'created_at', )
    search_fields = ('title', 'slug', )
    prepopulated_fields = {
        'slug': ['title'],
    }


admin.site.register(Course, CourseAdmin)
