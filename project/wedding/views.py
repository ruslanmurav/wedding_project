from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from wedding.models import Wedding, Comment, Photo, SitePhotos
from wedding.forms import CommentForm
from django.core.cache import cache


class MainView(TemplateView):
    template_name = 'wedding/main.html'
    title = 'Главная страница'

    def get_queryset(self):
        return Wedding.objects.order_by("-id")[:4]

    def get_wedding_photos(self, weddings):
        photos = Photo.objects.all()
        return {wedding: next((photo.photo_url for photo in photos if photo.wedding_id == wedding.id), None) for wedding in weddings}

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['title'] = self.title

        latest_weddings = self.get_queryset()
        context['weddings'] = latest_weddings

        wedding_photos = self.get_wedding_photos(latest_weddings)
        context['wedding_photos'] = wedding_photos

        comments = Comment.objects.filter(is_accepted=True)

        context['comments'] = comments

        context['form'] = CommentForm()

        all_photos = SitePhotos.objects.all()
        photo_dict = {}
        for photo in all_photos:
            photo_dict[photo.photo_name] = photo.site_photo

        context['site_photos'] = photo_dict


        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')



def pageNotFound(request, exception):
    context = {
        'title': 'Страница не найдена!'
    }
    return render(request, 'wedding/404.html', context)
