from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customers import Customer
from django.views import View

class Cubrix(View):
    def get(self,request):
        return render(request, 'cubrix.html')