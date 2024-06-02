from django.http import HttpResponse
from django.template.loader import get_template





class HomeView(): 

    def home (self):
        #vamos a pasar la plantilla por un generador de platillas
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())
    
    def formulario(self):
        plantilla = get_template('formulario.html').render()
        return HttpResponse(plantilla)
    
