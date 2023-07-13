from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'wedding/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['title'] = 'Главная страница'
        return context

