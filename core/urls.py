from django.urls import path
from weather.views.weatherView import WeatherCreate, WeatherReset, WeatherView, WeatherGenerate, WeatherUpdate, WeatherDelete
from uuid import UUID

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather-view'),
    path('weather/generate/', WeatherGenerate.as_view(), name='weather-generate'),
    path('weather/update/<str:uuid>/', WeatherUpdate.as_view(), name='weather-update'),
    path('weather/delete/<str:uuid>/', WeatherDelete.as_view(), name='weather-delete'),
    path('weather/reset/', WeatherReset.as_view(), name='weather-reset'),  
    path('weather/create/', WeatherCreate.as_view(), name='weather-create'), 
]
