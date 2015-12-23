from django.contrib import admin

from .models import Student
from .models import CourseProfile
from .models import CompleteData
from .models import YaleApiData

admin.site.register(Student)
admin.site.register(CourseProfile)
admin.site.register(CompleteData)
admin.site.register(YaleApiData)