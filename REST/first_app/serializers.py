from rest_framework import serializers
from first_app.models import Student, Collge
# class based
# car -- 

# DRY -- 

# video -- 1 
def name_startswith_R(value):
    if value[0].lower() == 'r':
        return value
    raise serializers.ValidationError("Name shud start with R or r")

def name_len(value):
    if len(value) >= 4:
        return value
    raise serializers.ValidationError("Len of name shud be always greater than 4")

from serializers import Serializer
"""
# ModelSerializer
class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[name_startswith_R, name_len])
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()

    def create(self, validated_data):
        stud = Student.objects.create(**validated_data)
        return stud

    def update(self, instance, validated_data):  # python dict
    
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)  # None
        instance.marks = validated_data.get('marks', instance.marks) # None
        instance.save()
        return instance

    # field level validation
    # def validate_age(self, value):
    #     print("validate age")
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("Age less than 21 is not allowed..")


    # def validate_marks(self, value):
    #     print("validate marks")
    #     return value

    # object level validation
    # def validate(self, data):
    #     print("in validate method")
    #     if (data.get("city") == "Pune") and (data.get("age") >= 21):
    #         return data
    #     raise serializers.ValidationError("City must be Pune and Age must be above 21")

"""

    

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, validators=[name_startswith_R, name_len])
    class Meta:
        model = Student 
        # fields = ['name', 'age','city', 'marks'] # 100 fields -- 
        fields = '__all__'
        # exclude = ['id', 'marks']
        # read_only_fields = ['name']
        # extra_kwargs = {"name": {'read_only': True}, "age": {"write_only": True}, "city": {'read_only': True}}

    # field level validation
    # def validate_age(self, value):
    #     print("validate age")
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("Age less than 21 is not allowed..")



class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collge 
        fields = '__all__'


from first_app.models import Track, Album
from rest_framework import serializers

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track 
        fields = ['order','title', 'duration' ]  # '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tracks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='track-detail')
    # tracks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # track_listing  = serializers.HyperlinkedIdentityField(view_name='track-detail')
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album 
        fields = ['id', 'album_name', 'artist', 'tracks'] #'__all__'   # related_name='tracks' 


