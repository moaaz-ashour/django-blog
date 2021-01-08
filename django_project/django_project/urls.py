from django.contrib import admin
from django.contrib.auth import views as auth_views # class_based build_in views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),   
    path('profile/', user_views.profile, name='profile'),
    path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),    
    path('', include('blog.urls')),
]
