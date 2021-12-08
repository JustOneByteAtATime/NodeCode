from django.urls import path
from .views import SignUpView, UserEditView, profile, ShowProfilePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/', profile, name='profile'),
    path('profile_page/<int:pk>', ShowProfilePageView.as_view(), name='profile_page')
]
