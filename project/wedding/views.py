from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from common.views import TitleMixin
from django.core.paginator import Paginator

from project.settings import BASE_DIR
from wedding.models import Wedding, Comment, Photo, SitePhotos, File
from wedding.forms import CommentForm
from django.core.cache import cache


class MainView(TitleMixin, TemplateView):
    template_name = 'wedding/main.html'
    title = 'Главная страница'

    def get_queryset(self):
        return Wedding.objects.order_by("-id")[:4]

    def get_sitephoto(self):
        all_photos = SitePhotos.objects.all()
        photo_dict = {}
        for photo in all_photos:
            photo_dict[photo.photo_name] = photo.site_photo
        return photo_dict

    def get_wedding_photos(self, weddings):
        photos = Photo.objects.all()
        return {wedding: next((photo.photo_url for photo in photos if photo.wedding_id == wedding.id), None) for wedding in weddings}

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        latest_weddings = self.get_queryset()
        context['weddings'] = latest_weddings

        wedding_photos = self.get_wedding_photos(latest_weddings)

        context['wedding_photos'] = wedding_photos

        comments = Comment.objects.filter(is_accepted=True)

        context['comments'] = comments

        context['form'] = CommentForm()

        context['site_photos'] = self.get_sitephoto()

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


class PortfolioView(TitleMixin, ListView):
    template_name = 'wedding/portfolio.html'
    model = Wedding
    title = 'Портфолио'
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            Prefetch('photo_set', queryset=Photo.objects.all()[:1], to_attr='photos')
        )


class WeddingView(TitleMixin, TemplateView):
    template_name = 'wedding/wedding_template.html'
    title = 'Свадьба'

    def get_files(self, **kwargs):
        files = File.objects.filter(wedding_id=kwargs['pk'], mark=1)
        return files

    def get_photos(self, **kwargs):
        photos = Photo.objects.filter(wedding_id=kwargs['pk'])
        return photos

    def get_context_data(self, **kwargs):
        context = super(WeddingView, self).get_context_data()
        context['pk'] = kwargs['pk']
        context['videos'] = self.get_files(**kwargs)
        context['photos'] = self.get_photos(**kwargs)
        return context


class AboutUsView(TitleMixin, TemplateView):
    template_name = 'wedding/about_us.html'
    title = 'О нас'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data()

        quote = File.objects.get(file_name='Цитата')
        about_us = File.objects.get(file_name='about_us')

        with open(f'media/{quote.file}', encoding='utf-8') as file:
            quote_text = file.read()
        with open(f'media/{about_us.file}', encoding='utf-8') as file:
            description = file.read()

        context['quote'] = quote_text
        context['text'] = description
        return context