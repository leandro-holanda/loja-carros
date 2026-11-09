from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import ProfileForm


class ProfileCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = ProfileForm()

        return render(
            request,
            'accounts/profile_create.html',
            {'form': form}
        )

    def post(self, request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('home')

        return render(
            request,
            'accounts/profile_create.html',
            {'form': form}
        )