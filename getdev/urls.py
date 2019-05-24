"""getdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="GetDev API Docs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/admin/',
    #      views.AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/user', views.UserSignUpView.as_view(), name='user_signup'),
    path('accounts/signup/admin',
         views.AdminSignUpView.as_view(), name='admin_signup'),
    path('docs/', schema_view)
]
