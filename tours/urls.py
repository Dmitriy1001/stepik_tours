from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view),
    path('departure/<str:departure>/', views.departure_view),
    path('tour/<int:id>/', views.tour_view),
]
