from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import User




from django.contrib.auth import authenticate, login, logout




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/'
    template_name = "registration/signup.html"
    
    def form_valid(self, form):
        valid = super().form_valid(form)

        # Login the user
        login(self.request, self.object)

        return valid