from django import forms

from brands.models import Brand


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError(
                'O nome da marca não pode ser vazio.'
            )

        return name.strip().upper()