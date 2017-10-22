from django.conf.urls import url
from .views import UserCreateView

urlpatterns = [
    url(r'^sign-up/', UserCreateView.as_view(), name='user_new'),
]
