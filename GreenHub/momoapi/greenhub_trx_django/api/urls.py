from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_api_app import views


router = routers.DefaultRouter()
router.register(r'users', views.MyUserViewSet)
router.register(r'transfers', views.TransferViewSet)
router.register(r'collections', views.CollectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns += router.urls