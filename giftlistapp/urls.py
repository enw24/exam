from giftlistapp import admin
from django.urls import path
from giftlistapp.views import ClothesList, ClothesDetail, VehicleList, VehicleDetail, JeweleryList, JeweleryDetail, PetList, PetDetail, OtherList, OtherDetail, Homepage

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('clothes/', ClothesList.as_view(), name="clothes_list"),
    path('clothes/<int:pk>/', ClothesDetail.as_view(), name='clothes_detail'),
    path('vehicle/', VehicleList.as_view(), name="vehicle_list"),
    path('vehicle/<int:pk>/', VehicleDetail.as_view(), name='vehicle_detail'),
    path('jewelry/', JeweleryList.as_view(), name="jewelry_list"),
    path('jewelry/<int:pk>/', JeweleryDetail.as_view(), name='jewelry_detail'),
    path('pet/', PetList.as_view(), name="pet_list"),
    path('pet/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('other/', OtherList.as_view(), name="other_list"),
    path('other/<int:pk>/', OtherDetail.as_view(), name='other_detail'),

]
