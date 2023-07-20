from django.db import models


class Wedding(models.Model):
    bride_name = models.CharField(max_length=255, verbose_name='Имя невесты')
    groom_name = models.CharField(max_length=255, verbose_name='Имя жениха')
    wedding_date = models.DateTimeField(verbose_name='Дата свадьбы', blank=True)
    wedding_location = models.CharField(max_length=255, verbose_name='Место проведения')
    wedding_description = models.TextField(verbose_name='Описание')



    class Meta:
        verbose_name = 'свадьбу'
        verbose_name_plural = 'Свадьбы'

    def __str__(self):
        return f"{self.bride_name.title()} + {self.groom_name.title()}"


class Comment(models.Model):
    commenter_name = models.CharField(max_length=255, verbose_name='Имя')
    commenter_avatar = models.ImageField(upload_to='commenter_avatar', blank=True, verbose_name='Аватар')
    comment_text = models.TextField(verbose_name='Текст')
    comment_date = models.DateTimeField(verbose_name='Дата создания')
    is_accepted = models.BooleanField(default=False, verbose_name='Статус модерации')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Комментарий от {self.commenter_name}"


class Photo(models.Model):
    wedding = models.ForeignKey(to=Wedding, on_delete=models.CASCADE, verbose_name='Свадьба')
    photo_url = models.ImageField(upload_to='wedding_photo', verbose_name='Аватар')
    photo_description = models.CharField(max_length=255, verbose_name='Описание')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f"Фото свадьбы: {self.wedding.bride_name} + {self.wedding.groom_name}"


class Moderate(Comment, models.Model):
    class Meta:
        proxy = True
        verbose_name = 'комментарий'
        verbose_name_plural = 'Модерация комментариев'


class SitePhotos(models.Model):
    photo_name = models.CharField(max_length=255)
    site_photo = models.ImageField(upload_to='site_photo')





