from django.core.files.storage import default_storage   #default_storage es la forma en que Django abstrae el sistema de archivos.
from django.http import HttpRequest 
from .interfaces import ImageStorage   #Importa la interfaz ImageStorage hecha en pages/interfaces.py

class ImageLocalStorage(ImageStorage):  #Creamos la clase que hereda de ImageStorage
    def store(self, request: HttpRequest):  #Implementa el método store de ImageStorage
        profile_image = request.FILES.get('profile_image', None)  #Obtiene el archivo de imagen request
        #request.FILES es un diccionario que contiene los archivos que se han subido a través de  un formulario HTML
        #'profile_image' Es el nombre del campo en el formulario
        #Si el archivo no existe retorna None
        
        if profile_image: #Verifica si subieron una imagen o es None   
            # Store the image
            file_name = default_storage.save('uploaded_images/' + profile_image.name, profile_image) #Crea el no0mbre del archivo con la ruta y lo guarda
            return default_storage.url(file_name)   #Convierte la ruta del archivo en una URL que se usará para mostrar la imagen en la página web
        
        