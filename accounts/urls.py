from django.urls import path
from accounts import views


from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path('accounts/signup', # caminho que vai carregar a view com o formulário
        views.AccountCreateView.as_view(),
        name="signup"
    ),
    path('account/<int:pk>/edit',
    views.AccountUpdateView.as_view(),
    name="account_edit"
    ),


]