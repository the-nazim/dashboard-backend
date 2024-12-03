from django.urls import path
from .views import user_list, signup, login_user, vehicle_profile, hello ,Home

urlpatterns = [
    path('users/', user_list, name='users'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path("vehicle-profile/", vehicle_profile, name='vehicle-profile'),
    path("test-vehicle/", hello, name="testhello"),
    path('', Home.as_view()),
]