from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from giftlistapp.models import Clothes, Jewelery, Vehicle, Pet, Other


class ClothesList(ListView):
    model=Clothes
    template_name="clothes_list.html"

class ClothesDetail(DetailView):
    model = Clothes
    template_name = "clothes_detail.html"


class JeweleryList(ListView):
    model = Jewelery
    template_name = "jewelery_list.html"


class JeweleryDetail(DetailView):
    model = Jewelery
    template_name = "jewelery_detail.html"


class VehicleList(ListView):
    model = Vehicle
    template_name = "vehicle_list.html"


class VehicleDetail(DetailView):
    model = Vehicle
    template_name = "vehicle_detail.html"


class PetList(ListView):
    model = Pet
    template_name = "pet_list.html"


class PetDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"


class OtherList(ListView):
    model = Other
    template_name = "other_list.html"


class OtherDetail(DetailView):
    model = Other
    template_name = "other_detail.html"

class Homepage(TemplateView):
    template_name = "home.html"