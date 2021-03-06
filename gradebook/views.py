# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from isis.gradebook.models import *
from isis.gradebook.forms import *

def dashboard(request):
  my_class_list = Class.objects.all().order_by('title')
  return render_to_response('gradebook/dashboard.html', {'my_class_list': my_class_list})
    
def gradebook(request, class_id):
  this_class = Class.objects.get(id=class_id)
  this_gradebook = this_class.gradebook
  my_class_list = Class.objects.all().order_by('title')
  my_student_list = this_class.students.all()
  return render_to_response('gradebook/gradebook.html', {'students': my_student_list, 'classes': my_class_list, 'this_class': this_class, 'this_gradebook': this_gradebook})

def class_add_student(request, class_id):
  this_class = Class.objects.get(id=class_id)
  this_gradebook = this_class.gradebook
  if request.method == 'POST':
    form = AddStudentToClass(request.POST)
    if form.is_valid():
      try:
	student = form.save()
	student.groups.add(group.objects.get(title='students'))
	student.save()
	this_class.students.add(student)
	this_class.save()
      except NameError:
	student.delete()
      return render_to_response('gradebook/gradebook.html')
  else:
      form = AddStudentToClass()
  return render_to_response('gradebook/student_form.html', {'form': form})
  
def class_add(request):
  if request.method == 'POST':
    form = TeacherClassEditForm(request.POST)
    if form.is_valid():
      # Add a new gradebook that automatically associates with the class, and gradescale that automatically associates with the gradebook.
      newclass = form.save()
      gscale = GradeScale()
      gb = Gradebook()
      newclass.gradebook = gb
      gscale.save()
      gb.grade_scale = gscale
      gb.save()
      newclass.save()
      return HttpResponseRedirect('/gradebook')
  else:
      form = TeacherClassEditForm()
  return render_to_response('gradebook/class_form.html', {'form': form})
