from django.contrib import admin

from .models import EvaluationComments
from .models import EvaluationCourseNames
from .models import EvaluationCourses
from .models import EvaluationProfessors
from .models import Student
from .models import CourseProfile
from .models import CompleteData
from .models import YaleApiData

admin.site.register(EvaluationComments)
admin.site.register(EvaluationCourseNames)
admin.site.register(EvaluationCourses)
admin.site.register(EvaluationProfessors)
admin.site.register(Student)
admin.site.register(CourseProfile)
admin.site.register(CompleteData)
admin.site.register(YaleApiData)