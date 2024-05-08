from users.views import user_login, conf_view, register_view, logout
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', register_view, name='signup'),
    path('conf/', conf_view, name='conf'),
    path('logout/',logout, name="logout")
]
