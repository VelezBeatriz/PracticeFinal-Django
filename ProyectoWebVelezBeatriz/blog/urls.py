from django.urls import path
from blog import views


# Sin la url de admin
urlpatterns = [

    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),

]


