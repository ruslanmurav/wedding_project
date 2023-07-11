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
    comment_id = models.AutoField(primary_key=True)  # Unique identifier for the comment
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=255)
    commenter_avatar = models.URLField()
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.comment_id} by {self.commenter_name} on {self.wedding.bride_name} & {self.wedding.groom_name}'s Wedding"

