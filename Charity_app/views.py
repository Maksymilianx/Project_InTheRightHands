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
        bags = Donation.objects.filter('quantity')
        return render(request, "base.html", {'bags': bags})


class CountOrganizations:
    def get(self, request):
        organizations = Institutions.objects.filter('name')
        return render(request, "base.html", {'organizations': organizations})