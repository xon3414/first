from django.urls import path
from .views import (
    ClientView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailView,
    ClientCreateView,
)

urlpatterns = [
    path('client', ClientView.as_view(), name="client_list"),
    path('client/new/', ClientCreateView.as_view(), name="client_new"),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client_detail"),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name="client_edit"),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name="client_delete"),
]