"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from pagesplay.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de services
    path('services/', include('services.urls')),
    # Paths de blog
    path('blog/', include('blog.urls')),
    # Paths de pages
    path('page/', include('pages.urls')),
    # Paths de pages
    path('contact/', include('contact.urls')),
# Paths de playground
    path('playground/', include('playground.urls')),
# Paths de playgroundpages
    path('pagesplay/', include(pages_patterns)),
# Paths de profiles
    path('profiles/', include(profiles_patterns)),
# Paths de messenger
    path('messenger/', include(messenger_patterns)),
    # Paths del admin
    path('admin/', admin.site.urls),
    # Paths del admin
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
