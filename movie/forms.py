from django import forms
from movie.models import Movie

class MovieForm(forms.ModelForm):

    title = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'placeholder': 'Movie title'}))
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Synopsis or description'}))
    actors = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'placeholder': 'Movie Actors'}))
    genre = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'placeholder': 'Genre'}))
    trailer = forms.CharField(max_length=255, required=True, widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'placeholder': 'Movie trailer link'}))
    poster = forms.CharField(max_length=255, required=True, widget=forms.widgets.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Blog title'}))

    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ("author",)
