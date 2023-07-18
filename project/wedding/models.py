from django.db import models


class Wedding(models.Model):
    bride_name = models.CharField(max_length=255)
    groom_name = models.CharField(max_length=255)
    wedding_date = models.DateTimeField()
    wedding_location = models.CharField(max_length=255)
    wedding_description = models.TextField()

    class Meta:
        verbose_name = 'свадьбу'
        verbose_name_plural = 'Свадьбы'

    def __str__(self):
        return f"{self.bride_name.title()} + {self.groom_name.title()}"


class Comment(models.Model):
    commenter_name = models.CharField(max_length=255)
    commenter_avatar = models.ImageField(upload_to='commenter_avatar', blank=True)
    comment_text = models.TextField()
    comment_date = models.DateTimeField()
    is_accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comment by {self.commenter_name}"


class Photo(models.Model):
    wedding = models.ForeignKey(to=Wedding, on_delete=models.CASCADE)
    photo_url = models.ImageField(upload_to='wedding_photo')
    photo_description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f"Photo for {self.wedding.bride_name} & {self.wedding.groom_name}'s Wedding"


class Moderate(Comment, models.Model):
    class Meta:
        proxy = True
        verbose_name = 'комментарий'
        verbose_name_plural = 'Модерация комментариев'


