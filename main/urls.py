from django.urls import path

from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView

app_name = 'main'

urlpatterns = [
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(http_method_names=['post','get','options']), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='change_password'),

    path('accounts/profile/', profile, name='profile'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]
