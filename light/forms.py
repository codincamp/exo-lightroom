from django.forms import ModelForm

from .models import Light

class LightForm(ModelForm):
    class Meta:
        model = Light
        fields = "__all__"
