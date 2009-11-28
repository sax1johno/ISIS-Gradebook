""" This class contains all of the forms required for the gradebook. """
from django.forms import ModelForm
from isis.gradebook.models import *

class TeacherClassEditForm(ModelForm):
  class Meta:
    model = Class
    exclude = ('gradebook', 'teacher')

class AddStudentToClass(ModelForm):
  class Meta:
    model = Student
    exclude = ('groups', 'date_joined', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'user_permissions')
