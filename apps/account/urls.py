from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from .views import (account_register, account_activete,dashboard,edit_details,delete_user,view_address,add_address,edit_address,delete_address,set_default,user_orders,wishlist,add_to_wishlist)
from .forms import PwdResetConfirmForm, PwdResetForm,UserLoginForm


app_name = "account"


urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="account/login.html", form_class=UserLoginForm),name="login"),
    path("loguot/",auth_views.LogoutView.as_view(next_page="/account/login/"), name="logout"),
    path("register/", account_register,name="register"),
    path("activate/<slug:uidb64>/<slug:token>/", account_activete, name="activate"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="account/password_reset/password_reset_form.html",
    success_url="password_reset_email_confirm",email_template_name="account/password_reset/password_reset_email.html", form_class=PwdResetForm),
    name="pwdreset"),
    path("password_reset_confirm/<uidb64>/<token>",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset/password_reset_confirm.html",
        success_url="password_reset_complete/",
        form_class=PwdResetConfirmForm,),name="password_reset_confirm",),
    path("password_reset_confirm/Mg/password_reset_complete/",TemplateView.as_view(template_name="account/password_reset/reset_status.html"),name="password_reset_complete",),
    # User dashboard
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/edit/",edit_details, name="edit_details"),
    path("profile/delete_user/", delete_user,name="delete_user"),
    path("profile/delete_confirm/",TemplateView.as_view(template_name="account/dashboard/delete_confirm.html"), name="delete_confirmation",),
    path("addresses/", view_address, name="addresses"),
    path("add_address/", add_address, name="add_address"),
    path("addresses/edit/<slug:id>/", edit_address, name="edit_address"),
    path("addresses/delete/<slug:id>/", delete_address, name="delete_address"),
    path("addresses/set_default/<slug:id>/", set_default, name="set_default"),
    path("user_orders/", user_orders,name="user_orders"),
    # Wish List
    path("wishlist", wishlist,name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>", add_to_wishlist,name="user_wishlist")
]



















































