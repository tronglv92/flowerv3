from rest_framework import serializers, status

from .models import Hoa


class CreateHoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoa
        fields = (
            'pk',
            'name',
            'number',)
