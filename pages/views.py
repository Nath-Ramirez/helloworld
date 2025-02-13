from django.shortcuts import render, redirect
#from django.http import HttpResponse #new
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django import forms
from django.views import View
from django.urls import reverse
from django import forms
# Create your views here.
#def homePageView(request):  #new
#    return HttpResponse("Hello World")  #new

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

class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":"$2000000"},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"$5000000"},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"$250000"},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"$90"}
    ]
    
class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    
    def get(self, request, id):
        try:
            id = int(id)  # Convertir el ID a entero
            if id < 1 or id > len(Product.products):  # Verificar si el ID está dentro del rango
                return HttpResponseRedirect(reverse('home'))  # Redirigir a home si no es válido

            product = Product.products[id - 1]
            viewData = {
                "title": product["name"] + " - Online Store",
                "subtitle": product["name"] + " - Product information",
                "product": product,
                "price": product["price"],
            }
            return render(request, self.template_name, viewData)
        
        except (ValueError, IndexError):  # Capturar errores de conversión o fuera de rango
            return HttpResponseRedirect(reverse('home'))  # Redirigir a home

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price
    
class ProductCreateView(View):
    template_name = 'products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('successful')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        
class ProductSuccessView(TemplateView):
    template_name = 'products/successful.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Success",
            "subtitle": "Product Created Successfully",
        })
        return context