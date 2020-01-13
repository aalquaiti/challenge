from rest_framework import serializers
from control.models import Control


class ControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Control
        # fields = ('name', 'type', 'maximum_rabi_rate', 'polar_angle')
        fields = '__all__'
