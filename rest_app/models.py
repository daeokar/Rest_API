from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()


    def __str__(self):
        return self.name


    class Meta:
        db_table = "stud"


class Collage(models.Model):
    name = models.CharField(max_length=100)
    staff_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "colg"




