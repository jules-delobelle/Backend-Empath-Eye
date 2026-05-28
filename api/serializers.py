from rest_framework import serializers
from .models import Session, Detection, Enfant

class EnfantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfant
        fields = "__all__"
        read_only_fields = ['id_user']


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = "__all__"


class DetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detection
        fields = "__all__"