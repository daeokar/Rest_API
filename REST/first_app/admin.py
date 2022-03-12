from django.contrib import admin
from first_app.models import Student, Collge, Album, Track
# Register your models here.


admin.site.register([Student, Collge, Album, Track])