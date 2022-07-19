from django.urls import path
from . import views

app_name = 'appLandLocator'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('lands', views.lands, name='lands'),
    path('land-details/codeL<int:landId>D', views.landDetails, name='landDetails'),
    path('upload-land', views.uploadLand, name='uploadLand'),
    path('delete-land/codeL<int:land_code>D', views.deleteLand, name='deleteLand'),
    path('update-land/codeL<int:land_code>D', views.updateLand, name='updateLand'),
]