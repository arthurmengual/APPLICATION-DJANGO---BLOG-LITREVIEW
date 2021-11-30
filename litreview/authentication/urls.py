from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True), name=('login')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('changepswd/',PasswordChangeView.as_view(template_name='authentication/changepswd.html'), name='changepswd' ),
    path('changepswddone/', PasswordChangeDoneView.as_view(template_name='authentication/changepswddone.html'), name='changepswddone'),
    path('photo/profile/change/', views.upload_profile_photo, name='change_profile_photo'),
]