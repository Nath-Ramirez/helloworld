from abc import ABC, abstractmethod #Importa la clase ABC (Abstract Base Class) y el decorador @abstractmethod del módulo abc
from django.http import HttpRequest #Importa la clase HttpRequest de Django.  Esta clase representa una solicitud HTTP 

#Las interfaces en programación son como contratos que especifican que métodos deben implementar las clases que las heredan 
class ImageStorage(ABC):    #Así se llamará la interfaz
    @abstractmethod   #Indica que el método decorado (store) es abstracto y debe ser implementado por una clase abstracta
    
    def store(self, request: HttpRequest):  #Define el método store que recibe una referencia de la clase y un objeto HTTP con la información
        pass    #El método no hace nada, las clases que implementen ImageStorage deberán definir su implementación

