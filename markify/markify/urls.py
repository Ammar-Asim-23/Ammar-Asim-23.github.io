from django.contrib import admin

from django.contrib.auth import views
from django.urls import path, include
from core.views import index, about, send_email
from userprofile.views import signup, my_account
from userprofile.forms import LoginForm


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/products/', include('product.urls')),
    path('dashboard/ads/', include('product.urls_ads')),
    path('dashboard/campaigns/', include('campaigns.urls')),
    path('dashboard/',include('userprofile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/',about,name="about"),
    path('send_email/',send_email,name="send_email"),
    path('sign-up/', signup,name="signup"),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=LoginForm), name="login"),
    path('log-out/',views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    
]
