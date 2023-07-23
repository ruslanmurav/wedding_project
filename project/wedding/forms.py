from django import forms
from wedding.models import Comment


class CommentForm(forms.ModelForm):
    commenter_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'user-name',
        'placeholder': 'Имя',
        'size': '53',
        'required': 'required',
    }))
    comment_date = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type': 'date',
        'id': 'marrige-date',
        'placeholder': 'Дата свадьбы',
        'required': 'required',
    }))
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'user-comment',
        'maxlength': '1000',
        'cols': '52',
        'rows': '10',
        'placeholder': 'Ваш комментарий',
        'required': 'required',
    }))

    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment_text', 'comment_date',)

