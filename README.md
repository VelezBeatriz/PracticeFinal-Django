# Apuntes para README.md

## Video 2

### Pasos para iniciar el proyecto:

```bash
django-admin startproject ProyectoWebVelezBeatriz
python manage.py startapp ProyectoWebappVelezBeatriz
python manage.py runserver
```

### Desarrollo de Vistas:

1. Agregar en el archivo `views.py` de la aplicación (`app`) el siguiente código para `httpResponse`:

    ```python
    from django.http import HttpResponse

    def mi_vista(request):
        return HttpResponse("¡Hola, mundo!")
    ```

2. Crear las vistas correspondientes y guardar los cambios.

3. Configurar las URLs correspondientes en el archivo `urls.py` del proyecto:

    ```python
    from django.urls import path
    from .views import mi_vista

    urlpatterns = [
        path('mi_ruta/', mi_vista, name='mi_vista'),
        # Agrega más rutas según sea necesario
    ]
    ```

Recuerda ajustar los nombres de las vistas y las rutas según tus necesidades específicas.

## Video 3


  
Recuerda que un proyecto Django puede tener múltiples aplicaciones, ya que muchas veces una aplicación puede ser reutilizable en diferentes proyectos.

### Configuración de URLs en la Aplicación de Django

1. Crear un archivo `urls.py` para la aplicación de Django.

2. Importar el `path` y las vistas al `urls.py` de la aplicación.

3. Copiar la lista de `urlpatterns` al archivo `urls.py` de la aplicación.

```python
# En urls.py de la aplicación
from django.urls import path
from . import views

urlpatterns = [
    # Agrega tus rutas y vistas aquí
]
```

4. Crear el path hacia el archivo de la aplicación, siguiendo la estructura recomendada.

```python
# En el archivo principal urls.py del proyecto
from django.urls import include, path

urlpatterns = [
    path('mi_app/', include('mi_app.urls')),
    # Agrega más rutas según sea necesario
]
```

### Configuración de Plantillas
- Crear una carpeta de templates en la aplicación.

- Añadir todas las plantillas correspondientes dentro de esta carpeta.

- Para que las plantillas se rendericen, ir a settings.py del proyecto y en la lista de INSTALLED_APPS registrar la aplicación.

```python

# En settings.py del proyecto
INSTALLED_APPS = [
    # ...
    'mi_app',
]
```


5. Ir a views.py y modificar las funciones para renderizar las plantillas. Ejemplo:

```python
# En views.py de la aplicación
from django.shortcuts import render

def contacto(request):
    return render(request, "mi_app/contacto.html")

```

## Video 4

Crear una carpeta en la aplicación para guardar todos los archivos descargados, que incluirán estilos, imágenes, etc.


Mis disculpas por la confusión. Aquí tienes el texto completo en formato Markdown:


## Video 5

En este video, aprenderemos a realizar las siguientes tareas:

### Cargar Contenidos Estáticos

Vamos a cargar los contenidos Static. Para lograrlo, añadiremos un tag en el encabezado para cargar estos datos antes de enlazar los estilos de Bootstrap. Recuerda que todos los enlaces provenientes de esta carpeta se verán de la siguiente forma:

```html
<link href="{% static 'ProyectoWebappVelezBeatriz/vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">
```

### Crear Plantilla Base

Crearemos una plantilla base donde guardaremos el encabezado, la barra de navegación y todo lo común para todas las plantillas. Recuerda que debes declarar el contenido de la web de la siguiente manera en la plantilla base:

```html
<!-- Contenido de la web -->
{% block content %}
<!-- Todo este código es diferente por sección -->
{% endblock %}
```

### Modificar URLs de la Barra de Navegación

Modificaremos las URLs de la barra de navegación desde la plantilla base. Por ejemplo:

```html
<a class="nav-link text-uppercase text-expanded" href="{% url 'Home' %}">Inicio</a>
```

Estos son los pasos que seguiremos en este video. ¡Continúa con el tutorial para más detalles!

Aquí está el texto proporcionado en formato Markdown:


## Video 6

En este video, añadiremos la acción de iluminación del navegador (nav) para la sección correspondiente. Por ejemplo:

```html
<li class="nav-item {% if request.path == '/' %}active{% endif %} px-lg-4">
```

Este código iluminará la pestaña de navegación cuando la URL actual coincida con la ruta especificada (en este caso, '/'). ¡Sigue con el tutorial para más detalles y personalización!


## Video 7


### Creación de Aplicaciones y Registro

En este paso, crearemos una aplicación separada para cada servicio en sí. Recuerda que debes registrar las aplicaciones.

Ahora nos dirigiremos a nuestra aplicación y buscaremos el archivo `models.py`. Dentro de este archivo, crearemos un mapeo ORM y a continuación definiremos los modelos utilizando clases y métodos.

Por ejemplo:

```python
# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo
```

Recuerda que para manejar imágenes, debes instalar el paquete Pillow de Python.

```bash
pip install Pillow
python manage.py makemigrations
python manage.py migrate
```

Este ejemplo representa la creación de un modelo llamado `Servicio` con atributos como `titulo`, `contenido`, `imagen`, `created`, y `updated`. Personaliza estos modelos según tus necesidades.


Aquí está el texto proporcionado en formato Markdown:


## Video 8

En este video, aprenderemos a realizar las siguientes tareas:

### Crear un Superusuario

Para crear un superusuario, ejecutaremos el siguiente comando en la terminal:

```bash
python manage.py createsuperuser
```

### Configurar la Sección Admin

Iremos al archivo `admin.py` e importaremos la aplicación llamada `servicios`. Ejemplo:

```python
from django.contrib import admin
from .models import Servicio

admin.site.register(Servicio)
```

### Personalizar la Interfaz del Administrador

Ahora especificaremos la personalización creando una clase que indique qué campos son de solo lectura al editar y borrar servicios. Ejemplo:

```python
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
```

Recuerda que puedes cambiar el idioma de la interfaz del administrador desde el archivo `settings.py`:

```python
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-EU'
```

Esto establece el idioma a español europeo. Ajusta el código de idioma según tus preferencias.


Video 9

Cuando estes en local recuerda que esta opcion debe ser cierta:
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

Al subirlo a produccion recuerda cambiar esto.

Imagenes y media
Crea una carpeta media para enviar todas las imagenes en cuestion a este directorio. Especifica en settings:
import os
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
y en el modelo especificar la ruta:
    imagen=models.ImageField(upload_to='servicios')


Pero la fotogrtafia sigue sin cargare, para ello haremos:


Cambiaras las urls generales por:
from django.urls import path
from ProyectoWebappVelezBeatriz import views
# Importar las rutas de media
from django.conf import settings
from django.conf.urls.static import static

# Sin la url de admin
urlpatterns = [
    path('', views.home, name="Home"),
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


Video 10

en views vamos a :
from servicios.models import Servicio
para obtener los datos y poder añadirlos en la plantilla correspondiente.

importaremos todos los objetos y que nos devuelva la plantilla y los servicios importados

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "ProyectoWebAppVelezBeatriz/servicios.html", {"servicios":servicios})
Finalmente podremso crear el blockcontent de servcios:
{% block content %}

    {% for servicio in servicios %}

    <div>
        <p>
            <h2 class="text-light">{{servicio.titulo}}</h2>
            <p class="text-light">{{servicio.contenido}}</p>
            <p><img src="media/{{servicio.imagen}}" alt="{{servicio.titulo}}"></p>
        </p>
    </div>
    {% endfor %}

Video 11

Migraremos la plantilla de servicios a la app correspondiente asi que nos tocara cambiar tadas las vistas, urls etc para poder visualizar correctamente la pagina:

Declaramos urls en servicios, eliminamos el servicio de donde no combiene.
en views de servicios declaramos:
from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})

en url servicios declaramos:
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

y en url general declaramos:
    path('servicios/', include('servicios.urls')),


video 12

Modificaremos los templates de servicios al gusto

Video 13

Vamos a crear el blog
Las entradas tendran categorias, titulos, contenido y fotografias para ello seguiremos los mismos pasos que hemos hecho ya en anteriores videos

Recuerda que este modelo trabaja con FK, aqui tienes un ejemplo:
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)

No te olvides declarar el modelo en admin.py para poder administrar el blog desde administracion de Django