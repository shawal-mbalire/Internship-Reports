from rest_framework import serializers
from rest_api_app.models import MyUser, Collection, Transfer


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone_num','first_name','last_name','email','password']