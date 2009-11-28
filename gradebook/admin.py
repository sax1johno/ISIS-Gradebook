from isis.gradebook.models import *
from django.contrib import admin

class TeacherAdmin(admin.ModelAdmin):
    pass
class StudentAdmin(admin.ModelAdmin):
  pass
  
class GradeBracketInline(admin.TabularInline):
  model = GradeBracket
  extra = 10
  
class GradeScaleAdmin(admin.ModelAdmin):
  inlines = [GradeBracketInline]

admin.site.register(Term)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class)
admin.site.register(Gradebook)
admin.site.register(GradeScale, GradeScaleAdmin)
#admin.site.register(GradeBracket)
admin.site.register(Assignment)
admin.site.register(AssignmentType)
admin.site.register(AssignmentScore)