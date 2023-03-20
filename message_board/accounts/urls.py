from django.urls import path
from .views import SignUp, AccountsList

urlpatterns = [
    path('', AccountsList.as_view(), name='accounts_list'),
    path('signup/', SignUp.as_view(), name='signup'),
]