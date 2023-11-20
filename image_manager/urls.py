from django.urls import path
from .views import dashboard, admin_dashboard, login_view, logout_view, register_view

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    # path('upload-image/', upload_image, name='upload_image'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
