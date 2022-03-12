from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'stud'


class Collge(models.Model):
    name = models.CharField(max_length=100)
    staff_count = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'colg'



from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Django Signals

# generate token using django signal -- Tokene generated right after creating User Object
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=Student)
def say_hello(sender, instance=None, created=False, **kwargs):
    if created:
        print(f"Hello Good Morning... {instance.name}!")

@receiver(post_delete, sender=Student)
def say_bye(sender, instance=None, **kwargs):
    print(kwargs)
    print(f"Bye Bye... {instance.name}!")



class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name
    class Meta:
        db_table = 'album'


class Track(models.Model):
    order = models.IntegerField()  
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']
        db_table = 'track'


    def __str__(self):
        return f"{self.order}  ---  {self.title}"

