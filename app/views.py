from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class cbncontent(TemplateView):
    template_name="cbncontent.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Gracy'
        context['age']=20
        return context