from django.urls import path, include
from user.userView import UserLogin, UserRegister
from weather.views.weatherView import WeatherCreate, WeatherReset, WeatherView, WeatherGenerate, WeatherUpdate, WeatherDelete
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather-view'),
    path('weather/generate/', WeatherGenerate.as_view(), name='weather-generate'),
    path('weather/update/<str:uuid>/', WeatherUpdate.as_view(), name='weather-update'),
    path('weather/delete/<str:uuid>/', WeatherDelete.as_view(), name='weather-delete'),
    path('weather/reset/', WeatherReset.as_view(), name='weather-reset'),  
    path('weather/create/', WeatherCreate.as_view(), name='weather-create'),
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
