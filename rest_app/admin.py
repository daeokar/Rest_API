from django.contrib import admin
from rest_app.models import *

# Register your models here.

admin.site.register([Student, Collage, Album, Track])


# >>> from rest_app.models import *
# >>> Student.objects.all()
# <QuerySet [<Student: AAA>, <Student: BBB>]>
# >>> Student.objects.get(id=1)
# <Student: AAA>

