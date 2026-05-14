from rest_framework import serializers
from .models import Profil, Session, Detection, Enfant

class ProfilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profil
        fields = "__all__"
        extra_kwargs = {"motdepasse": {"write_only": True}}
        

class EnfantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enfant
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = "__all__"


class DetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detection
        fields = "__all__"