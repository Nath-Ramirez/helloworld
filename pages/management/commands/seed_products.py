#Importa la clase BaseComand la cual es usada para crear comandos de administración personalizados en Django
from django.core.management.base import BaseCommand 
#Importa la clase ProductFactory de el archivo factories.py dentro de la app pages.
#factories.py contiene la definición de la fábrica para el modelo Product (con factory_boy). 
#Esta fábrica se utilizará para crear los productos de ejemplo
from pages.factories import ProductFactory

#La clase Command hereda de BaseCommand. Esta clase representa el comando de administración personalizado que vas a crear.
class Command(BaseCommand): 
    #Define el atributo help. Este atributo contiene una descripción breve del comando, que se mostrará cuando ejecutes python manage.py help
    help = 'Seed the database with products'
    
    #Este método contiene la lógica principal del comando. Se ejecuta cuando llamas al comando desde la línea de comandos (python manage.py seed_products)
    def handle(self, *args, **kwargs):
        #Esta es la línea clave, ProductFactory es la fábrica que importé anteriormente
        #create_batch es el método de factory_boy que crea 8 instancias del modelo Product utilizando la definición de la fábrica ProductFactory
        #Cada instancia se guardará en la base de datos. Los valores para los campos de cada producto se generarán automáticamente 
        # según lo definido en ProductFactory (usando Faker o valores estáticos, según cómo esté configurada tu fábrica)
        ProductFactory.create_batch(8)
        #Esta línea muestra un mensaje en la consola indicando que el proceso de "sembrado" (creación de datos de ejemplo) se ha completado correctamente
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))
        
        