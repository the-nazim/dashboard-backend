from django.urls import path
from .views import user_list, signup, login_user

urlpatterns = [
    path('users/', user_list, name='users'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login')
]