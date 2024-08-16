"""
URL configuration for MINING_UNIVERSITY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
import debug_toolbar
from django.conf.urls.static import static
from contact_form.views import ContactCreate, success

from MINING_UNIVERSITY import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('graduates_list/', include('graduates.urls', namespace = 'graduates_list')),
    path('user/', include('users.urls', namespace = 'user')),
    path('poll/', include('polls.urls', namespace = 'poll')),
    path('poll_company/', include('polls_company.urls', namespace = 'poll_company')),
    # path('contact_form/', include('contact_form.urls', namespace = 'contact_form')),
    path('contact_page/', ContactCreate.as_view(), name ='contact_page'),
    path('feedback/', include('feedback.urls', namespace = 'feedback')),
    path('success/', success, name='success_page')
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
