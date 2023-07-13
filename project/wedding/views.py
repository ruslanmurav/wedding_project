from django.shortcuts import render
from django.views.generic import TemplateView
from wedding.models import Wedding

class MainView(TemplateView):
    template_name = 'wedding/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['title'] = 'Главная страница'
        last_id = Wedding.objects.last().id
        set = Wedding.objects.filter(id__gt=last_id-4)
        context['weddings'] = set

        return context

