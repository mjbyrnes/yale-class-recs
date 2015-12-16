from django.db import models
from django.forms import ModelForm
from .models import Student, CourseProfile

class StudentForm(ModelForm):
  class Meta:
    model = Student
    fields = ['first_name','last_name','grad_year','major']
    labels = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'grad_year': 'Graduation Year',
    'major': 'Major',
    }

class CourseForm(ModelForm):
  class Meta:
    model = CourseProfile
    fields = ['average_rating','average_difficulty','num_students','skill','area']
    labels = {
    'average_rating': 'Average Rating',
    'average_difficulty': 'Average Difficulty',
    'num_students': 'Approximate Number of Students',
    'skill': "Skills Requirement",
    'area': "Area Requirement",
    }
