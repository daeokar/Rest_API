from rest_framework import serializers
from rest_app.models import *
# class based


#----validations

def name_startswith_A(value):
    if value[0].lower() == "a":
        return value
    raise serializers.ValidationError("Name shuold be start with A or a")

def name_len(value):
    if len(value) >= 4:
        return value
    raise serializers.ValidationError("The len of the Name should be greater than 4 or equal to 4")

"""

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[name_startswith_A, name_len])
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()


    def create(self, validated_data):
        stud = Student.objects.create(**validated_data)
        return stud


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.save()
        return instance

    #---field level validations
    # def validate_age(self, value):
    #     print("in validate")
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("Age less than 21 is not allowed....!")



    def validate_marks(self, value):
        print("Validate Marks")
        return value


        #-----object_level validations
    def validate(self, data):
        print(" In the object level validation ")
        if (data.get("city") == "Pune") and (data.get("age") >= 21):
            return data

        raise serializers.ValidationError(" City must be Pune and age must be Greater than equal to the 21")

"""


# --ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, validators=[name_startswith_A, name_len])
    class Meta:
        model = Student
        # fields = ["id", "name", "age", "city", "marks"]
        fields = "__all__"
        # exclude = ["id", "marks"]
        # read_only_fields = ["name"]
        # extra_kwargs = {"name" : {"read_only":True}, "age" : {"write_only":True}}

    # def validate_age(self, value):
    #     print("validate age")
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("Age less than 21 is not allowed...!")

