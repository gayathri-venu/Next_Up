from django.urls import path, include
from .views import HomePageView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup', SignUpView.as_view(), name='signup'),
]
