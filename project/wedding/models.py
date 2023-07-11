from django.db import models

# Create your models here.


class Wedding(models.Model):
    bride_name = models.CharField(max_length=255)
    groom_name = models.CharField(max_length=255)
    wedding_date = models.DateTimeField()
    wedding_location = models.CharField(max_length=255)
    wedding_description = models.TextField()

    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}'s Wedding"