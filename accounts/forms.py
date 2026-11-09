from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileForm(forms.ModelForm):

    cpf = forms.CharField(max_length=11)
    city = forms.CharField(max_length=100)
    neighborhood = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    phone = forms.CharField(max_length=20)

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return password_confirm

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError('CPF inválido.')

        if Profile.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado.')

        return cpf

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False

        if commit:
            from django.db import transaction

            with transaction.atomic():
                user.save()

                Profile.objects.create(
                    user=user,
                    cpf=self.cleaned_data['cpf'],
                    city=self.cleaned_data['city'].upper(),
                    neighborhood=self.cleaned_data['neighborhood'].upper(),
                    state=self.cleaned_data['state'].upper(),
                    phone=self.cleaned_data['phone'],
                )

        return user