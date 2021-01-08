import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
SECRET_KEY='!=ayd1f0u=0-!%zj1276d7(i!6z&92owbuo#91qbr4v5%_bgrg'
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contentypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE=[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.comtrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF='my_site.urls'
TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"html"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'content_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION='my_site.wsgi.application'
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS={
    {
        'NAME':'django.contrib.auth.passord_validation.UserAttributesSimilarityValidator',
    },
    {
        'NAME':'django.contrib.auth.passord_validation.MinimumLengthValidator',
    },
    {
        'NAME':'django.contrib.auth.passord_validation.CommonPasswordValidator',
    },
    {
        'NAME':'django.contrib.auth.passord_validation.NumericPasswordValidator',
    },
}
LANGEUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_L10N=True
USE_TZ=True
STATIC_URL='/static/'