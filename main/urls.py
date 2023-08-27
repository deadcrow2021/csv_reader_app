from django.urls import path
from . import views


urlpatterns = [
    path('overview/', views.api_overview, name="api-overview"),
    path('deals/', views.deals_list, name="list"),
    path('create/', views.add_deals, name='add-deals'),
    path('', views.main, name='main'),
]
