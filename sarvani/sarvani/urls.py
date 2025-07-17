"""
URL configuration for sarvani project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name ="home"),
    path('su/', success, name ="su"),
    path('admin/', admin.site.urls),
    path('contact/', contact, name ="contact"),
    path('about/', about, name ="about"),
    path('login/', login_page, name ="login"),
    path('logout/', logout_page, name ="logout"),
    path('register/', register, name ="register"),
    path('feedback/', student_feedback, name='student_feedback'),

    path('receipes/', receipes, name ="receipes"),
    path('users/',include('users.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()