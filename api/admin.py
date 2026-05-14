from django.contrib import admin
from .models import Profil, Session, Detection, Enfant

admin.site.register(Profil)
admin.site.register(Enfant)
admin.site.register(Session)
admin.site.register(Detection)