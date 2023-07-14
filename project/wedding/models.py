from django.db import models


class Wedding(models.Model):
    bride_name = models.CharField(max_length=255)
    groom_name = models.CharField(max_length=255)
    wedding_date = models.DateTimeField()
    wedding_location = models.CharField(max_length=255)
    wedding_description = models.TextField()

    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}'s Wedding"


class Comment(models.Model):
    wedding = models.ForeignKey(to=Wedding, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=255)
    commenter_avatar = models.ImageField(upload_to='commenter_avatar', blank=True)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.commenter_name} on {self.wedding.bride_name} & {self.wedding.groom_name}'s Wedding"


class Photo(models.Model):
    wedding = models.ForeignKey(to=Wedding, on_delete=models.CASCADE)
    photo_url = models.ImageField(upload_to='wedding_photo')
    photo_description = models.CharField(max_length=255)

    def __str__(self):
        return f"Photo for {self.wedding.bride_name} & {self.wedding.groom_name}'s Wedding"


class Moderate(Comment, models.Model):
    class Meta:
        proxy = True

