from django.shortcuts import render
from django.views import View

from Charity_app.models import Donation, Institutions


class LandingPage(View):
    def get(self, request):
        return render(request, "base.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")


class CountBags(View):
    def get(self, request):
        queryset = list(Donation.objects.all())
        return render(request, "base.html", {'queryset': queryset})


class CountOrganizations:
    def get(self, request):
        lst = list(Institutions.objects.all())
        return render(request, "base.html", {'lst': lst})