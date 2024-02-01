from django.urls import path
from ProyectoWebappVelezBeatriz import views
# Importar las rutas de media
from django.conf import settings
from django.conf.urls.static import static

# Sin la url de admin
urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
]


