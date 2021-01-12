
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
# router.register('words', views.WordView)
# router.register('translation', views.TransView)
# router.register('lang', views.LangView)


app_name = 'api'

urlpatterns = [
	path('', include(router.urls)),
]
