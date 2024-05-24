from datetime import datetime
from random import choice, randrange
from django.shortcuts import render, redirect
from django.views import View
from ..repositories.weatherRepository import WeatherRepository
import uuid

class WeatherView(View):
    """
    Exibe a página inicial com os dados meteorológicos.

    Método HTTP GET:
    - Retorna todos os dados meteorológicos se não houver filtro por cidade.
    - Retorna os dados meteorológicos filtrados por cidade se houver um parâmetro 'city' na requisição GET.
    """
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        city = request.GET.get('city')
        weathers = repository.filter_by_city(city) if city else repository.get_all()
        return render(request, "home.html", {"weathers": weathers})

class WeatherGenerate(View):
    """
    Gera dados meteorológicos aleatórios e insere no banco de dados.

    Método HTTP GET:
    - Gera um conjunto de dados meteorológicos aleatórios.
    - Insere os dados gerados no banco de dados.
    - Redireciona para a página de visualização de dados meteorológicos.
    
    Método HTTP POST:
    - Extrai os dados meteorológicos da requisição POST.
    - Insere os dados extraídos no banco de dados.
    - Redireciona para a página de visualização de dados meteorológicos.
    """
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather_data = self.generate_random_weather()
        repository.insert(weather_data)
        return redirect('weather-view')

    def post(self, request):
        weather_data = self.extract_weather_data_from_request(request)
        repository = WeatherRepository(collectionName='weathers')
        repository.insert(weather_data)
        return redirect('weather-view')

    def generate_random_weather(self):
        return {
            "uuid": str(uuid.uuid4()),
            "temperature": randrange(17, 40),
            "city": choice(["Sorocaba", "Alumínio", "Mairinque"]),
            "atmospheric_pressure": randrange(800, 1200),
            "humidity": randrange(30, 90),
            "weather": choice(["Ensolarado", "Nublado", "Chuvoso"]),
            "date": datetime.now(),
            "last_updated": datetime.now()
        }

    def extract_weather_data_from_request(self, request):
        return {
            "uuid": str(uuid.uuid4()),
            "temperature": request.POST.get('temperature'),
            "city": request.POST.get('city'),
            "atmospheric_pressure": request.POST.get('atmospheric_pressure'),
            "humidity": request.POST.get('humidity'),
            "weather": request.POST.get('weather'),
            "date": datetime.strptime(request.POST.get('date'), '%d-%m-%Y'),
            "last_updated": datetime.now()
        }

class WeatherUpdate(View):
    """
    Atualiza dados meteorológicos existentes no banco de dados.

    Método HTTP POST:
    - Extrai os dados meteorológicos da requisição POST.
    - Atualiza os dados no banco de dados com base no UUID fornecido.
    - Redireciona para a página de visualização de dados meteorológicos.
    """
    def extract_weather_data_from_request(self, request):
        temperature = request.POST.get('temperature')
        city = request.POST.get('city')
        atmospheric_pressure = request.POST.get('atmospheric_pressure')
        humidity = request.POST.get('humidity')
        weather = request.POST.get('weather')
        date = datetime.now()

        weather_data = {
            "temperature": temperature,
            "city": city,
            "atmospheric_pressure": atmospheric_pressure,
            "humidity": humidity,
            "weather": weather,
            "last_updated": date
        }
        return weather_data

    def post(self, request, uuid):
        try:
            weather_data = self.extract_weather_data_from_request(request)
            repository = WeatherRepository(collectionName='weathers')
            
            filter_query = {"uuid": uuid}
            update_query = weather_data
            
            repository.update(filter_query, update_query)
            return redirect('weather-view')
        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect('weather-view')


class WeatherDelete(View):
    """
    Exclui dados meteorológicos do banco de dados.

    Método HTTP POST:
    - Exclui os dados com base no UUID fornecido.
    - Redireciona para a página de visualização de dados meteorológicos.
    """
    def post(self, request, uuid):
        repository = WeatherRepository(collectionName='weathers')
        repository.delete({"uuid": uuid})
        return redirect('weather-view')

class WeatherReset(View):
    """
    Reinicia todos os dados meteorológicos no banco de dados.

    Método HTTP POST:
    - Exclui todos os dados meteorológicos do banco de dados.
    - Redireciona para a página de visualização de dados meteorológicos.
    """
    def post(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.delete_all()
        return redirect('weather-view')

class WeatherCreate(View):
    """
    Cria dados meteorológicos e insere no banco de dados.

    Método HTTP POST:
    - Extrai os dados meteorológicos da requisição POST.
    - Insere os dados extraídos no banco de dados.
    - Redireciona para a página de visualização de dados meteorológicos.
    """
    def extract_weather_data_from_request(self, request):
        temperature = int(request.POST.get('temperature'))
        city = request.POST.get('city')
        atmospheric_pressure = int(request.POST.get('atmospheric_pressure'))
        humidity = int(request.POST.get('humidity'))
        weather = request.POST.get('weather')

        date = datetime.now()
        weather_uuid = str(uuid.uuid4())

        weather_data = {
            "uuid": weather_uuid,
            "temperature": temperature,
            "city": city,
            "atmospheric_pressure": atmospheric_pressure,
            "humidity": humidity,
            "weather": weather,
            "date": date,
            "last_updated": date    
        }
        return weather_data

    def post(self, request):
        try:
            weather_data = self.extract_weather_data_from_request(request)
            repository = WeatherRepository(collectionName='weathers')
            repository.insert(weather_data)
            return redirect('weather-view')
        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect('weather-view')
