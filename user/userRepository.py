import logging
from django.contrib.auth.hashers import check_password as django_check_password
from django.conf import settings
import pymongo

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

class UserRepository:
    def __init__(self):
        self.collection_name = 'users'
        self.client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        self.db = self.client[getattr(settings, "MONGO_DATABASE_NAME")]
        self.collection = self.db[self.collection_name]

    def get_user_by_email(self, email):
        user = self.collection.find_one({"email": email})
        return user

    def check_password(self, user_email, entered_password):
        user = self.collection.find_one({"email": user_email})

        if user and 'password' in user:
            stored_hash = user['password']
            logger.info(f'Usuário recuperado: {user_email}')
            logger.info(f'Senha hashada no banco de dados: {stored_hash}')
            if django_check_password(entered_password, stored_hash):
                logger.info('Senha correta')
                return user
            else:
                logger.warning('Senha incorreta')
        else:
            logger.warning('Usuário não encontrado ou senha não definida')

        return None

    def get_all_users(self):
        users = self.collection.find({})
        return list(users)

    def create_user(self, user_data):
        result = self.collection.insert_one(user_data)
        return result.inserted_id

    def update_user(self, email, update_data):
        result = self.collection.update_one({"email": email}, {"$set": update_data})
        return result.modified_count

    def delete_user(self, email):
        result = self.collection.delete_one({"email": email})
        return result.deleted_count

