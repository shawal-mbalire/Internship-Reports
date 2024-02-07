We create a python virtual environment to install the required packages for the project. 

```bash 
python -m venv .venv
```
```bash 
.venv\Scripts\activate
```
We install the required packages using the following command. 
```bash
pip install -r requirements.txt
```
We can create a django project using the following command. 
```bash
django-admin startproject greenhub_trx
```

Next we edit the database settings of the django application to include the database credentials. 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'greenhub',
        'USER': 'api_user',
        'PASSWORD': 'api_user_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

We edit allowed hosts in the settings.py file to include the domain name of the server. 
```python

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```