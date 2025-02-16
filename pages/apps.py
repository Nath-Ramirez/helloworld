from django.apps import AppConfig
from django.utils.module_loading import import_string #Para cargar clases y funciones a partir de su ruta en forma de cadena
from django.conf import settings    #Importa las configuraciones incluyendo la clase que administra las imágenes (IMAGE_STORAGE_CLASS)

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'    
    name = 'pages'

    #Este método se llama cuando Django está listo, justo antes de que la aplicación comience a recibir solicitudes
    def ready(self):
        ImageStorageClass = import_string(settings.IMAGE_STORAGE_CLASS)
        #Obtiene el valor de la configuración; luego, con import_string toma la cadena (ruta de la clase) e importa la clase correspondiente
        
    