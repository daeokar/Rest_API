from rest_framework import serializers
from rest_app.models import *
# class based

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()


    def create(self, validated_data):
        stud = Student.objects.create(**validated_data)
        return stud

