from django.shortcuts import render, redirect, get_object_or_404 #new
#from django.http import HttpResponse 
from django.views.generic import TemplateView, ListView #new
from django.http import HttpResponseRedirect
from django import forms
from django.views import View
from django.urls import reverse
from django import forms
from .models import Product #new
# Create your views here.
#def homePageView(request):  
#    return HttpResponse("Hello World")  

class HomePageView(TemplateView):
    template_name='home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact",
            "Email": "This is my email: pepito@eafit.edu.co",
            "Address": "This is my address: Los Angeles con la minorista",
            "Phone": "This is my phone number: 36915248",
        })
        return context
    
class ProductIndexView(View):
    template_name = 'products/index.html' #Especifica la plantilla html que se utilizará para renderizar la vista
    
    def get(self, request):
        viewData = {}   #Diccionario vacío que se usará para pasarle dats a la plantilla
        viewData["title"] = "Products - Online Store" #Título de la página
        viewData["subtitle"] = "List of products" #Subtítulo de la página
        viewData["products"] = Product.objects.all() #Se consulta a la base de datos para obtener todos los objetos Product 
        
        return render(request, self.template_name, viewData) #Se renderiza la plantilla especificada y se le pasa el diccionario 
    
class ProductShowView(View):
    template_name = 'products/show.html' #Especifica la plantilla html que se utilizará
    
    def get(self, request, id): #El id que recibe en la URL se usa para identificar el producto que se va a mostrar
        try:
            product_id = int(id)  # Convertir el ID a entero
            if product_id < 1:  # Verificar si el ID está dentro del rango
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id) #Se utilizaq la función "get_object_or_404" para obtener el objeto Product
                                                                #cuyo id (pk) coincide con product_id. Si no lo encuentra lanza un error 404
        
        except (ValueError, IndexError):  # Capturar errores de conversión o fuera de rango
            return HttpResponseRedirect(reverse('home'))  # Redirigir a home
        
        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] = product.name + " - Product information"
        viewData["product"] = product #Se añade el objeto product encontrado anteriormente para pasar por medio del diccionario a la plantilla
        
        return render(request, self.template_name, viewData)

class ProductForm(forms.ModelForm): #Hereda de ModelForm porque trabajamos con un modelos de BD
    class Meta:
        model = Product #Indica que este formulario está basado en el modelo "Product"
        fields = ['name','price'] #Solo incluirá los datos "name" y "price"
        
    def clean_price(self): #Validar el precio antes de guardarlo
        price = self.cleaned_data.get("price") #Obtiene el valor ingresado en "price"
        if price <= 0 and price is not None: #Verifica si el precio es válido
            raise forms.ValidationError("The price must be greater than zero.") #Muestra un error si no es válido 
        return price #Si todo está bien, devuelve el precio sin cambios
    
class ProductCreateView(View): 
    template_name = 'products/create.html' #Indica la plantilla html donde se mostrará el formulario
    
    def get(self, request):
        form = ProductForm() #Crea una instancia vacía del formulario
        viewData = {}   #Se crea un diccionario con datos para la plantilla 
        viewData["title"] = "Create product"
        viewData["form"] = form #Se pasa el formulario a la plantilla para que se muestre
        return render(request, self.template_name, viewData)
    
    def post(self, request):    #Cuando el usuario envía el formulario
        form = ProductForm(request.POST) #Rellena el formulario con los fatos enviados
        if form.is_valid(): #Verifica si los datos son válidos (precio > 0, etc)
            form.save()     #Lo guarda en la BD
            return redirect('successful') #Redirige a la página de éxito 
        else:
            viewData = {}
            viewData["title"] = "Create product"    #Si el formulario tiene errores se vuelve a mostrar con los mensajes de error
            viewData["form"] = form
            return render(request, self.template_name, viewData) #Reenvía la págian con errores visibles
        
class ProductSuccessView(TemplateView):
    template_name = 'products/successful.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Success",
            "subtitle": "Product Created Successfully",
        })
        return context
    
class ProductListView(ListView):
    model = Product #Le dice a Django que esta vista trabajará con el modelo Product
    template_name = 'product_list.html' #Especifica la plantilla html que utilizará
    context_object_name = 'products' #Define el nombre de la variable que se utilizará en la plantilla para acceder a la lista de productos

    def get_context_data(self, **kwargs): #Este método permite añadir datos adicionales al contexto que se pasa a la plantilla.
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products - Online Store'
        context['subtitle'] = 'List of products'
        return context
    
class CartView(View):   #Vista principal del carrito 
    template_name = 'cart/index.html' #Especifica la plantilla html que se utilizará para renderizar el carrito

    def get(self, request): #Este método maneja cuando el usuario visita la página del carrtio (get)
        # Simulated database for products
        products = {}   #Simula una base de datos de productos. En una app real, esto se reemplazaría con una consulta a tu modelo de datos de productos 
        products[121] = {'name': 'Tv samsung', 'price': '1000'} #Ejemplo de un producto en el "catálogo"
        products[11] = {'name': 'Iphone', 'price': '2000'}  
        # Get cart products from session
        cart_products = {}  #Diccionario para almacenar los productos que están actualmente en el carrito del usuario
        cart_product_data = request.session.get('cart_product_data', {})   
        #Recupera los datos del carrito de la sesión del usuario. request.session es la forma en que Django maneja las sesiones.
        #'cart_product_data' es la clave que se utiliza para almacenar los datos del carrito en la sesión. Si no existe nada en la sesión, 
        #se inicializa con un diccionario vacío 
        
        for key, product in products.items():   #Itera sobre los productos disponibles
            if str(key) in cart_product_data.keys(): #Comprueba si el id del producto está en el carrito almacenado en la sesión (se guarda como string)
                cart_products[key] = product    #Si el producto está en el carrito, se agrega al diccionario 'cart_products'
                
        # Prepare data for the view
        view_data = {   #Diccionario que s ele pasará a la plantilla
        'title': 'Cart - Online Store',
        'subtitle': 'Shopping Cart',
        'products': products,   #Todos los productos
        'cart_products': cart_products  #Los productos del carrito
        }
        return render(request, self.template_name, view_data)   #Renderiza la plantilla
    def post(self, request, product_id):   #Este método maneja cuando el usuario agrega un producto al carrito (post)
        # Get cart products from session and add the new product
        cart_product_data = request.session.get('cart_product_data', {})   #Obtiene los datos del carrito de la sesión, o de un diccionario vacío
        cart_product_data[product_id] = product_id  #Agrega el product_id al diccionario cart_product_data
        #Aquí se está usando el product_id como clave y como valor. En una app real, podrías guardar más información del producto en el carrito
        request.session['cart_product_data'] = cart_product_data    #Guarda los datos actualizados del carrito en la sesión
        return redirect('cart_index')   #Redirige al usuario a la página del carrito 'cart_index'

class CartRemoveAllView(View):  #Vista para vaciar el carrito
    def post(self, request):    #Maneja las solicitudes post para vaciar el carrito
    # Remove all products from cart in session
        if 'cart_product_data' in request.session:  #Verifica si existen datos del carrito en la sesión 
            del request.session['cart_product_data']    #Elimina los datos del carrito de la sesión
        return redirect('cart_index')   ##Redirige al usuario a la página del carrito 
    
