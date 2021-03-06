"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
#from django.urls import url , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name= 'home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    re_path(r'^test/$',views.TestPage.as_view(), name='test'),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^groups',include('groups.urls',namespace='groups')),
    re_path(r'^thanks/$',views.ThanksPage.as_view(), name='thanks'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
