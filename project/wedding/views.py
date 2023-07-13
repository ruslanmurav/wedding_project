from django.shortcuts import render
from django.views.generic import TemplateView
from wedding.models import Wedding, Comment


class MainView(TemplateView):
    template_name = 'wedding/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['title'] = 'Главная страница'
        latest_weddings = Wedding.objects.none() if Wedding.objects.count() == 0 else Wedding.objects.order_by("-id")[:4]
        context['weddings'] = latest_weddings
        comments = Comment.objects.all()
        context['comments'] = comments
        return context



