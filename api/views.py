from django.shortcuts import render
from .models import Session, Detection, Enfant
from .serializers import SessionSerializer, DetectionSerializer, EnfantSerializer
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# Create your views here.

class RegisterView (views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):    
        username = request.data["username"]
        password = request.data["password"]
        try:
            User.objects.create_user(username=username, password=password)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    

class EnfantViewSet(viewsets.ModelViewSet):
    serializer_class = EnfantSerializer

    def get_queryset(self):
        return Enfant.objects.filter(id_user = self.request.user)

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        enfants = Enfant.objects.filter(id_user = self.request.user)
        return Session.objects.filter(id_enfant = enfants)


class DetectionViewSet(viewsets.ModelViewSet):
    serializer_class = DetectionSerializer

    def get_queryset(self):
        enfants = Enfant.objects.filter(id_user = self.request.user)
        sessions = Session.objects.filter(id_enfant = enfants)
        return Detection.objects.filter(id_session = sessions)
