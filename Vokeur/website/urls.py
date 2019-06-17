from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("kieswijzer/", views.kieswijzer, name="kieswijzer"),
  path("verenigingen/<str:name>/", views.verenigingen, name="verenigingen"),
  path("contact/", views.contact, name="contact"),
  path("vereniging/<str:url>/", views.vereniging, name="vereniging"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
