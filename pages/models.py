from django.db import models

# Create your models here.
#Se define un modelo llamado producto. Product hereda de models.Model y así obtiene todo lo necesario para interactuar con la BD
# a través del ORM (Object-Relational Mapper) de Django
class Product(models.Model):
    name = models.CharField(max_length=255) #name representa el nombre del producto, CharFiel especifica que son caracteres
    price = models.IntegerField() #price representa el precio del producto, IntegerField especifica que es un entero
    created_at = models.DateTimeField(auto_now_add=True)  #created_at almacena la fecha y hora de la creación del producto
    #auto_now_add=True Le dice a Django que establezca automáticamente la fecha y hora actual en el momento en que se crea el 
    #registro del producto por primera vez. Este valor no se actualizará automáticamente cuando se modifique el producto.
    updated_at = models.DateTimeField(auto_now=True) #update_at almacena la fecha y hora en que se actualizó por última vez el producto
    
class Comment(models.Model):    #Define un modelo llamado "Comment" y crea una tabla en la BD que hereda los métodos de models.Model
    #Crea una relación con el modelo Product (un comentario pertenece a un producto)
    #Product -> Indica que el comentario está vinculado a un producto específico
    #on_delete=models.CASCADE → Si el producto es eliminado, sus comentarios también se eliminan automáticamente.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #Define un campo descripción para almacenar el texto del comentario
    description = models.TextField()
