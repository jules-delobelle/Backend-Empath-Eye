from django.db import models

class Profil(models.Model):
    id_profil = models.CharField(max_length=30, primary_key=True)
    motdepasse = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table= "Profils"

class Enfant(models.Model):
    id_enfant = models.AutoField(primary_key=True)
    id_profil = models.ForeignKey(Profil, on_delete=models.CASCADE, db_column="id_profil")
    naissance = models.DateField(null=True, blank=True)
    prenom = models.CharField(max_length = 50)

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
        ("peur", "Peur")
    ]
    emotion = models.CharField(max_length = 20, choices=EMOTIONS)
    heure = models.DateTimeField()
    landmarks = models.JSONField()
    important = models.BooleanField(default=False)

    class Meta:
        db_table = "Detections"