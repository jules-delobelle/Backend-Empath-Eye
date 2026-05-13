from django.db import models

class Profil(models.Model):
    id_profil = models.CharField(max_length=30, primary_key=True)
    motdepasse = models.CharField(max_length=255)
    naissance = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table= "Profils"


class Session(models.Model):
    id_session = models.AutoField(primary_key=True)
    id_profil = models.ForeignKey(Profil, on_delete=models.CASCADE, db_column='id_profil')
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
        ("peur", "Peur")
    ]
    heure = models.DateTimeField()
    landmarks = models.JSONField()
    important = models.BooleanField()

    class Meta:
        db_table = "Detections"