from django.urls import include, path
from django_prometheus import exports as django_prometheus_exports

urlpatterns = [
    path('', include('meu_app.urls')),
    path('', include('django_prometheus.urls')),
]