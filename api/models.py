from django.db import models
from django.contrib.auth.models import User


class Enfant(models.Model):
    id_enfant = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="id_user")
    naissance = models.DateField(null=True, blank=True)
    prenom = models.CharField(max_length = 50)
    dernier_telechargement = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table= "Enfant"


class Session(models.Model):
    id_session = models.AutoField(primary_key=True)
    id_enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, db_column='id_enfant')
    date = models.DateField()

    class Meta:
        db_table = "Sessions"

class Detection(models.Model):
    id_detection = models.AutoField(primary_key=True)
    id_session = models.ForeignKey(Session, on_delete=models.CASCADE, db_column='id_session')
    EMOTIONS = [
        ("joie", "Joie"),
        ("tristesse", "Tristesse"),
        ("colere", "Colere"),
        ("surprise", "Surprise")
    ]
    emotion = models.CharField(max_length = 20, choices=EMOTIONS)
    heure = models.DateTimeField()
    important = models.BooleanField(default=False)

    class Meta:
        db_table = "Detections"