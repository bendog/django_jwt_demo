from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('', include(router.urls)),
]