from django import forms
from wedding.models import Comment


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment_text', 'comment_date', 'commenter_avatar')

