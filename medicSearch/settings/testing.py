from.settings import *
DEBUG = True
#chave secreta
SECRET_KEY = 'ra5rar3ajhb'
#conectar no banco sqllite3
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#conectar no banco mysql
# DATABASE={
#     'default': {
#         'ENGINE': 'django.db.backends.MYSQL',
#         'NAME': 'medicdb',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306',
# }
# }
ALLOEWD_HOSTS=['localhost', '127.0.0.1']