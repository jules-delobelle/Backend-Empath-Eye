from django.shortcuts import render
from .models import Profil, Session, Detection, Enfant
from .serializers import ProfilSerializer, SessionSerializer, DetectionSerializer, EnfantSerializer
from rest_framework import viewsets

# Create your views here.

class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class= ProfilSerializer

class EnfantViewSet(viewsets.ModelViewSet):
    queryset = Enfant.objects.all()
    serializer_class = EnfantSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class DetectionViewSet(viewsets.ModelViewSet):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
