from django.urls import path

from .views import home_views

from .views.search_views import Homies , Person 

from .views import Blood_views






urlpatterns = [
  
    path('mhssscbatch', home_views.Home_items.as_view(), name = 'home'),
    path('all_homies_info', Homies, name = 'homies'),
    path('homies_<int:id>', Person, name = "person"),
  
    path('blood', Blood_views.Blood_group.as_view(), name = 'blood'),

   
   
]
