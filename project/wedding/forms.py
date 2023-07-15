from django import forms
from wedding.models import Comment


class CommentForm(forms.Form):
    class Meta:
        # model = Comment
        # fields = ('')
        pass
