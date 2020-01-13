# Created by: Aymen Al-Quaiti
# For QCTRL Backend Challenge
# January  2020
"""
Contains all Serializers used by Models in app
"""

from rest_framework import serializers
from .models import Control

class ControlSerializer(serializers.ModelSerializer):
    """
    Serializer for Control Model. All fields are required
    """

    class Meta:
        model = Control
        fields = '__all__'
