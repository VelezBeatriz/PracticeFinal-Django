from django.urls import path
from . import views
# Importar las rutas de media
from django.conf import settings
from django.conf.urls.static import static

# Sin la url de admin
urlpatterns = [
    path('', views.servicios, name="Servicios"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)