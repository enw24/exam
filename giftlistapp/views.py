from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from giftlistapp.models import Clothes, Jewelery, Vehicle, Pet, Other

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Form()
    return render(request, 'clothes_list.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


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

class CreatePurchaseList(CreateView):
    model = Purchased
    template_name = "purchased.html"
    success_url = reverse_lazy("homepage")
    fields = ['info']
