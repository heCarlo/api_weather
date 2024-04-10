from datetime import datetime
from random import choice, randrange
from django.views import View
from django.shortcuts import render, redirect
from ..repositories.weatherRepository import WeatherRepository
import uuid

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        city = request.GET.get('city')
        if city:
            weathers = repository.filter_by_city(city)
        else:
            weathers = repository.get_all()
        return render(request, "home.html", {"weathers": weathers})

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather_data = {
            "uuid": str(uuid.uuid4()),  # Gerando um novo UUID
            "temperature": randrange(17, 40),  # Temperatura aleatória entre 17 e 40
            "city": choice(["Sorocaba", "Alumínio", "Mairinque"]),  # Escolha aleatória de cidade
            "atmospheric_pressure": randrange(800, 1200),  # Exemplo de pressão atmosférica aleatória
            "humidity": randrange(30, 90),  # Exemplo de umidade aleatória
            "weather": choice(["Ensolarado", "Nublado", "Chuvoso"]),  # Escolha aleatória de clima
            "date": datetime.now(),
            "last_updated": datetime.now()  
        }
        repository.insert(weather_data)
        return redirect('weather-view')
    
    def post(self, request):
        temperature = request.POST.get('temperature')
        city = request.POST.get('city')
        atmospheric_pressure = request.POST.get('atmospheric_pressure')
        humidity = request.POST.get('humidity')
        weather = request.POST.get('weather')
        date = request.POST.get('date')
        
        # Convertendo a string de data para um objeto datetime
        date = datetime.strptime(date, '%d-%m-%Y')
        
        repository = WeatherRepository(collectionName='weathers')
        weather_data = {
            "uuid": str(uuid.uuid4()),  # Gerando um novo UUID
            "temperature": temperature,
            "city": city,
            "atmospheric_pressure": atmospheric_pressure,
            "humidity": humidity,
            "weather": weather,
            "date": date.strftime('%d/%m/%Y %H:%M:%S'),  # Formato 24h
            "last_updated": datetime.now().strftime('%d/%m/%Y %H:%M:%S')  
        }
        repository.insert(weather_data)
        return redirect('weather-view')
    
class WeatherUpdate(View):
    def post(self, request, uuid):
        try:
            temperature = request.POST.get('temperature')
            city = request.POST.get('city')
            atmospheric_pressure = request.POST.get('atmospheric_pressure')
            humidity = request.POST.get('humidity')
            weather = request.POST.get('weather')
            date = request.POST.get('date')
            
            # Convertendo a string de data para um objeto datetime
            date = datetime.strptime(date, '%Y-%m-%d')
            
            repository = WeatherRepository(collection_name='weathers')
            filter_query = {"uuid": uuid}
            update_query = {
                "temperature": temperature,
                "city": city,
                "atmospheric_pressure": atmospheric_pressure,
                "humidity": humidity,
                "weather": weather,
                "date": date,  # Removendo a formatação da data
                "last_updated": datetime.now()  
            }
            repository.update(filter_query, update_query)
            return redirect('weather-view')
        except Exception as e:
            # Lidar com qualquer exceção aqui
            # Por exemplo, você pode querer registrar o erro para depuração
            print(f"Ocorreu um erro: {e}")
            # Redirecionar de volta para a página do formulário com uma mensagem de erro
            return redirect('weather-view')  # Redirecionamento temporário

class WeatherDelete(View):
    def post(self, request, uuid):
        repository = WeatherRepository(collectionName='weathers')
        query = {"uuid": uuid}
        repository.delete(query)
        return redirect('weather-view')

class WeatherReset(View):
    def post(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.delete_all()
        return redirect('weather-view')

class WeatherCreate(View):
    def post(self, request):
        temperature = request.POST.get('temperature')
        city = request.POST.get('city')
        atmospheric_pressure = request.POST.get('atmospheric_pressure')
        humidity = request.POST.get('humidity')
        weather = request.POST.get('weather')
        date = request.POST.get('date')
        
        try:
            # Inicializando a variável uuid antes do processamento do formulário
            weather_uuid = str(uuid.uuid4())  # Gerando um novo UUID
            
            # Convertendo a string de data para um objeto datetime
            date = datetime.strptime(date, '%Y-%m-%d')
            
            repository = WeatherRepository(collectionName='weathers')
            weather_data = {
                "uuid": weather_uuid,
                "temperature": temperature,
                "city": city,
                "atmospheric_pressure": atmospheric_pressure,
                "humidity": humidity,
                "weather": weather,
                "date": date.strftime('%d/%m/%Y %H:%M:%S'),  # Formato 24h
                "last_updated": datetime.now().strftime('%d/%m/%Y %H:%M:%S')  
            }
            repository.insert(weather_data)
            return redirect('weather-view')
        except Exception as e:
            # Lidar com qualquer exceção aqui
            # Por exemplo, você pode querer registrar o erro para depuração
            print(f"Ocorreu um erro: {e}")
            # Redirecionar de volta para a página do formulário com uma mensagem de erro
            return render(request, "weather_create.html", {"error": "Ocorreu um erro ao processar o formulário. Por favor, tente novamente."})
