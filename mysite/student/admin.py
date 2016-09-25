from django.contrib import admin
from .models import Student, Grade
# Register your models here.

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 3

class StudentAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Basic information', {'fields': ['name', 'gender', 'birth_date']}),
        ('School information', {'fields': ['school', 'major'], 'classes': ['collapse']}),   
    ]
    list_display = ['name', 'gender', 'birth_date', 'school', 'major']
    list_filter = ['gender']
    search_fields = ['name']
    inlines = [GradeInline]

class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'score']


admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
