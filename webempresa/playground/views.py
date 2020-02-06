from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


#todo convertir todas las vbf a vbc en todas las apps(urgente)
#vistas basadas en clases modo de empleo
class PlaygroundPageView(TemplateView):

    template_name = "playground/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"LA VARIABLE PASADA AL TEMPLATE"})


class SamplePageView(TemplateView):

    template_name = "playground/sample.html"
