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
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password :
            return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.create_user(username=username, password=password)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EnfantViewSet(viewsets.ModelViewSet):
    serializer_class = EnfantSerializer

    def get_queryset(self):
        return Enfant.objects.filter(id_user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user)

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer

    def get_queryset(self):
        enfant = self.request.query_params.get("enfant")
        if enfant:
            return Session.objects.filter(id_enfant=enfant, id_enfant__id_user=self.request.user)
        else:
            enfants = Enfant.objects.filter(id_user=self.request.user)
            return Session.objects.filter(id_enfant__in=enfants)


class DetectionViewSet(viewsets.ModelViewSet):
    serializer_class = DetectionSerializer

    def get_queryset(self):
        session = self.request.query_params.get("session")
        important = self.request.query_params.get("important")
        if important == "true":
            enfants = Enfant.objects.filter(id_user=self.request.user)
            sessions = Session.objects.filter(id_enfant__in=enfants)
            return Detection.objects.filter(id_session__in=sessions, important=True)
        elif session:
            return Detection.objects.filter(id_session = session, id_session__id_enfant__id_user = self.request.user)
        else:
            enfants = Enfant.objects.filter(id_user = self.request.user)
            sessions = Session.objects.filter(id_enfant__in = enfants)
            return Detection.objects.filter(id_session__in = sessions)
        
class StatsView(views.APIView):
    def get(self, request):
        enfant_id = self.request.query_params.get("enfant")
        if enfant_id == None:
            return Response({"error": "erreur lors du chargement de l'enfant"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            enfant = Enfant.objects.get(id_enfant=enfant_id, id_user=request.user)
        except Enfant.DoesNotExist:
            return Response({"error": "erreur lors du chargement de l'enfant"}, status=status.HTTP_400_BAD_REQUEST)
        
        sessions = list(Session.objects.filter(id_enfant=enfant).order_by('-date')[:7])
        detections = Detection.objects.filter(id_session__in=sessions)

        stats = {"joie": 0, "tristesse": 0, "colere": 0, "surprise": 0}

        for detection in detections:
            stats[detection.emotion] += 1
        
        return Response(stats)

