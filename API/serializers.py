
import re
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields= ['uid','title','description','completed','due_date']  


#validating data with the help of regular expression in serializer

    # def validate(self, data):
    #     if not re.match(r'^[A-Z][a-z]{2,}', data['title']):
    #         raise serializers.ValidationError("Title must be start with capital letter and minimum 3 characters")
    #     return data