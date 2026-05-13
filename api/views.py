from django.shortcuts import render
from .models import Profil, Session, Detection
from .serializers import ProfilSerializer, SessionSerializer, DetectionSerializer
from rest_framework import viewsets

# Create your views here.

class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class= ProfilSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class DetectionViewSet(viewsets.ModelViewSet):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
