from django import forms
from .models import ModelCar


class ModelCarForm(forms.ModelForm):

    class Meta:
        model = ModelCar
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('O nome do modelo deve conter pelo menos uma letra.')
        return name.strip().upper() if name else name