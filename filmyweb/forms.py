from django.forms import ModelForm
from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        # exclude = []
        fields = ['title', 'year', 'description',
                  "premiere", "imbd_rating", "picture"]
