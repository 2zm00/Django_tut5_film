# forms.py
from django import forms
from .models import Review, Comment, Film

class ReviewForm(forms.ModelForm):
    film = forms.ModelChoiceField(
        queryset=Film.objects.all(),
        label='영화',
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-blue-500'
        })
    )

    class Meta:
        model = Review
        fields = ['film', 'title', 'content', 'rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }