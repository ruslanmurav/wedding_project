from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from wedding.models import Wedding, Comment, Photo
from wedding.forms import CommentForm


class MainView(TemplateView):
    template_name = 'wedding/main.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['title'] = 'Главная страница'
        latest_weddings = Wedding.objects.none() if Wedding.objects.count() == 0 else Wedding.objects.order_by("-id")[:4]
        context['weddings'] = latest_weddings
        photos = Photo.objects.all()
        first_photos = {}
        for wedding in latest_weddings:
            for photo in photos:
                if photo.wedding_id == wedding.id and wedding not in first_photos:
                    first_photos[wedding] = photo.photo_url
        context['first_photos'] = first_photos
        comments = Comment.objects.filter(is_accepted=1)
        context['comments'] = comments
        context['form'] = CommentForm()
        return context


def pageNotFound(request, exception):
    return render(request, 'wedding/404.html')






