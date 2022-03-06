from rest_framework import serializers

# class based

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()

