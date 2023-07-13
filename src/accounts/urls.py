from django.urls import path
from .views import signup, my_profile

app_name='accounts'
urlpatterns = [

    path('signup', signup, name='signup'),
    path('<slug:slug>', my_profile, name='profile')

]


