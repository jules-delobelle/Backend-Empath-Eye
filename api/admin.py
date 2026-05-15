from django.contrib import admin
from .models import Session, Detection, Enfant

admin.site.register(Enfant)
admin.site.register(Session)
admin.site.register(Detection)