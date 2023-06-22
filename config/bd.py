import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'smt',

        'USER': 'postgres',

        'PASSWORD': '@samuel_c22@',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}


POSTGRESQLSERVER = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'smt',

        'USER': 'postgres',

        'PASSWORD': '1234',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}
