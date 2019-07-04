from rest_framework import routers, serializers, viewsets
from .models import KonUser, AssetPackage, Lesson
from konapp import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
class KonUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }
        

class AssetPackageSerializer(serializers.HyperlinkedModelSerializer):
  
   
    author = KonUserSerializer()

    class Meta:
        model = AssetPackage
        fields = ['id','title','description','image','asset','price','author','created_date','modified_date']   
        read_only_fields = ('author','created_date','modified_date')
   

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','title', 'description', 'image', 'content','author','assets','created_date','modified_date')
        read_only_fields = ('author','created_date','modified_date')
