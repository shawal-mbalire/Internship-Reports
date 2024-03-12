from rest_framework import serializers
from rest_api_app.models import MyUser, Collection, Transfer


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'



class TransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'


