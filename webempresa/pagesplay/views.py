from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import PageForm

# Create your views here.
#TODO ARREGLAR URGENTE ERROR EN CODIGOFUENTE  #envs/django2/lib/site-packages/django/forms/boundfield.py LINEA 93 COMENTADO NO DEBERIA ESTAR COMENTADO ENTENDER QUE PASO
class StaffRequieredMixin(object): #object hereda de todas las clases de django
    """este mixin lo que hace es requerir al usuario que sea miembro del estaff"""
    @method_decorator(staff_member_required)#method decorator es el metodo de implementar un decorador y staffmemeberrequired es el decorador usado
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequieredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
   model = Page
   template_name = "pagesplay/pages.html"

class PageDetailView(DetailView):
    model = Page
    template_name = "pagesplay/page.html"

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pagesplay:pagesplay')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pagesplay:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pagesplay:pagesplay')