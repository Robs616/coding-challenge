from rest_framework import serializers

from .models import Buzzword

#serializer for list api buzzword 
class BuzzwordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buzzword
        fields = ('name', 'description')

		