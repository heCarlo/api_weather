import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from user.token import generate_jwt_token
from .userRepository import UserRepository
from uuid import uuid4
from rest_framework_simplejwt.tokens import RefreshToken

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

class UserRegister(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        try:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            logger.info(f'Registrando usuário com email: {email}, username: {username}')

            if not email or '@' not in email:
                logger.error('Email inválido fornecido.')
                raise ValueError('Por favor, insira um email válido.')

            user_repo = UserRepository()
            existing_user = user_repo.get_user_by_email(email=email)
            if existing_user:
                logger.error('Email já está em uso.')
                raise ValueError('Este email já está em uso. Por favor, escolha outro.')

            hashed_password = make_password(password)
            new_user_data = {
                'uuid': str(uuid4()),
                'email': email,
                'username': username,
                'password': hashed_password,
            }
            user_repo.create_user(new_user_data)

            logger.info(f'Usuário registrado com sucesso: {email}')
            return redirect('login')
        except Exception as e:
            logger.error(f'Erro ao registrar usuário: {e}')
            return render(request, 'login.html', {'error': str(e)})

class UserLogin(View):
    def post(self, request):
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            logger.info(f'Tentativa de login com email: {email}')

            user_repo = UserRepository()
            user = user_repo.get_user_by_email(email)
            if user and user['uuid'] and check_password(password, user['password']):
                logger.info(f'Usuário {user["username"]} fez login com sucesso.')

                # Gerar o token JWT utilizando a função importada
                token = generate_jwt_token(user['uuid'])

                return JsonResponse({'token': token})  # Retorna o token para o frontend
            else:
                raise ValueError('Credenciais inválidas. Por favor, tente novamente.')
        except Exception as e:
            logger.error(f'Erro ao fazer login: {e}')
            return JsonResponse({'error': str(e)}, status=400)
