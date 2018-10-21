import django

SECRET_KEY = 'stuffandnonsense'

APPS = [
    'nano.activation',
    'nano.badge',
    'nano.blog',
    'nano.chunk',
    'nano.comments',
    'nano.comments.tests',
    'nano.countries',
    'nano.faq',
    'nano.mark',
    'nano.mark.tests',
    'nano.privmsg',
    'nano.tools',
    'nano.tools.tests',
    'nano.user',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
] + APPS

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'tests.urls'
