
import factory
from .models import Product #Este es el modelo que se utilizará para crear los objetos 

#La clase ProductFactory hereda de factory.django.DjangoModelFactory, esta herencia le dice a factory_boy que esta fábrica
#se utilizará para crear instancias de un modelo de Django.
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta: #Esta clase está creada dentro de la clase ProductFactory y sirve para configurar el comportamiento de la fábrica
        model = Product #Esto le dice a ProductFactory que los objetos que creará serán instancias del modelo Product
    name = factory.Faker('company')  #Esta línea define cómo se generará el valor del campo name del modelo Product
    price = factory.Faker('random_int', min=200, max=9000) # Esta línea define cómo se generará el valor del campo price del modelo Product
    