"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
# from item import views as ItemViews
from django_registration.backends.one_step.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalog/', include('item.urls'), name='cat'),
    # path('catalog/', views.catalog, name='catalog'),
    # path('item/<int:item_id>/', ItemViews.item_details, name='item-details'),
    # path('item/add/', ItemViews.add_item, name='add-item'),
    path('warehouse/', include('warehouse.urls')),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'mysite.views.error_404_view'
