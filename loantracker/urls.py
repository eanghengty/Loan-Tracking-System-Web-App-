from django.contrib import admin
from django.urls import path
from clients.views import add_client
from dashboard.views import dashboard
urlpatterns = [
    path('admin/',admin.site.urls),
    path('add-client/',add_client,name='add-client'),
    path('',dashboard,name='dashboard')
]