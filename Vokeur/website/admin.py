from django.contrib import admin
from .models import Vragen, Antwoorden, Stad, Verenigingen, Letter, Woorden

# Register your models here.

admin.site.register(Vragen)
admin.site.register(Antwoorden)
admin.site.register(Stad)
admin.site.register(Verenigingen)
admin.site.register(Letter)
admin.site.register(Woorden)
