from django.http import HttpResponse
from django.views.generic import ListView
from .models import UserModel



class HomeView(ListView):
    model = UserModel



