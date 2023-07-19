from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('class/banks/', include('banks.class_urls')),
    path('function/banks/', include('banks.function_urls')),
    path('class/accounts/', include('accounts.class_urls')),
    path('function/accounts/', include('accounts.function_urls')),
]
