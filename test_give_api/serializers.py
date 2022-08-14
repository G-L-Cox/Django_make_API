from rest_framework import serializers
from .models import stuff_temp



class stuff_temp_serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stuff_temp
        fields = ('id', 'url', 'name', 'stuff', 'num')













