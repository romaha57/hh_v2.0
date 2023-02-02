from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import User
from .forms import ProfileChangeForm


class ProfileView(UpdateView):
    model = User
    form_class = ProfileChangeForm
    template_name = 'app_users/profile_user.html'

    def get_success_url(self):
        return reverse_lazy('app_users:profile', args=(self.request.user.id,))
