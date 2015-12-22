from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserForm, StudentForm, CourseForm, WeightForm
from .models import Student, CompleteData
from . import score_calc as sc

class CoverView(generic.ListView):
  template_name = "yale_class_recs/cover.html"
  def get_queryset(self):
    return None

def about(request):
  return render(request, 'yale_class_recs/about.html', {})

def search(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')
  
  # saves course to worksheet
  save_course = request.POST.get("class", False)
  if save_course:
    x = Student.objects.get(user=request.user)
    saves = x.get_courses()
    temp = []
    for num in saves:
      temp.append(num)
    temp.append(int(save_course))
    x.saved_courses = temp
    x.save()
    return HttpResponseRedirect('/yale_class_recs/worksheet')

  if request.method == 'POST':
    form = CourseForm(request.POST)
    form2 = WeightForm(request.POST)
    if form.is_valid() and form2.is_valid():
      return search_results(request)

  form = CourseForm()
  form2 = WeightForm()
  return render(request, 'yale_class_recs/search.html', {'form': form, 'form2': form2,})

def search_results(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')

  form = CourseForm(request.POST)
  form2 = WeightForm(request.POST)
  if form.is_valid() and form2.is_valid():
    difficulty = form.cleaned_data['difficulty']
    rating = form.cleaned_data['rating']
    size = form.cleaned_data['size']
    day = form.cleaned_data['day']

    start_time = form.cleaned_data['start_time']
    end_time = form.cleaned_data['end_time']
    times = (start_time, end_time)
    area = form.cleaned_data['area']
    skills = form.cleaned_data['skills']
    keywords = form.cleaned_data['keywords']
    major = form.cleaned_data['major']
    weights = [
      form2.cleaned_data['difficulty_weight'],
      form2.cleaned_data['rating_weight'],
      form2.cleaned_data['size_weight'],
      form2.cleaned_data['time_weight']
    ]
    results = sc.match_score_calc(difficulty, rating, area, skills, keywords, day, times, size, major, weights, request)
    return render(request, 'yale_class_recs/search_results.html', {'total': str(len(results)), 'course_results': results})

  form = CourseForm()
  form2 = WeightForm()
  return render(request, 'yale_class_recs/search.html', {'form': form, 'form2': form2,})

def course_info(request, course_id):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')

  course = CompleteData.objects.get(id=course_id)
  return render(request, 'yale_class_recs/course_info.html', {'course': course,})

def get_new_user_info(request):
  error = 0

  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      grad_year = form.cleaned_data['grad_year']
      major = form.cleaned_data['major']
    else:
      error = "Be sure to fill in all of the fields!"

    form = UserForm(request.POST)
    if form.is_valid() and error == 0:
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      if User.objects.filter(username=username).count() != 0:
        error = "The username you selected is already in use. Please choose a new one"
      elif password != form.cleaned_data['confirm_password']:
        error = "The passwords entered do not match"
      else:
        new_user = User.objects.create_user(username, email=None, password=password, first_name=first_name, 
          last_name=last_name)
        new_user.save()
        student = Student.objects.create(first_name=first_name, last_name=last_name,
          grad_year=grad_year, major=major, user=new_user)
        student.save()
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/yale_class_recs/accounts/profile')
          else:
            error = "An account for this user already exists, but it is deactivated"
        else:
          error = "There was a problem creating your account. Please try again"

    else:
      error = "Be sure to fill in all of the fields!"


  form = UserForm()
  form2 = StudentForm()
  context = {
    'form': form,
    'form2': form2,
    'error': error,
  }
  return render(request, 'yale_class_recs/user_info.html', context)

def user_home(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')

  student = Student.objects.get(user=request.user)
  context = {
    'first_name': student.first_name,
    'last_name': student.last_name,
    'grad_year': student.grad_year,
    'major': student.major,
    'username': request.user.username,
  }
  return render(request, 'yale_class_recs/user_home_page.html', context)

def edit_info(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')

  student = Student.objects.get(user=request.user)

  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      student.first_name = form.cleaned_data['first_name']
      student.last_name = form.cleaned_data['last_name']
      student.grad_year = form.cleaned_data['grad_year']
      student.major = form.cleaned_data['major']
      student.save()
    return HttpResponseRedirect('/yale_class_recs/accounts/profile/')

  form = StudentForm({'first_name': student.first_name, 'last_name': student.last_name,
    'grad_year': student.grad_year, 'major': student.major})
  context = {
    'form': form,
  }
  return render(request, 'yale_class_recs/edit_info.html', context)

def worksheet(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')

  # remove classes from worksheet
  delete_course = request.POST.get("class", False)
  if delete_course:
    x = Student.objects.get(user=request.user)
    saves = x.get_courses()
    temp = []
    for num in saves:
      if num == int(delete_course):
        pass
      else:
        temp.append(num)
    x.saved_courses = temp
    x.save()
    return HttpResponseRedirect('/yale_class_recs/worksheet')

  # display classes to user  
  saved = Student.objects.get(user=request.user).get_courses()
  cd = CompleteData.objects.filter(pk__in=saved)

  context = {
    'saved': saved,
    'CD': cd,
  }
  return render(request, 'yale_class_recs/worksheet.html', context)