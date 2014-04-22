import sys

import django
from django.conf import settings

APPS = [
    'nano.activation',
    'nano.badge',
    'nano.blog',
    'nano.chunk',
    'nano.comments',
    'nano.countries',
    'nano.faq',
    'nano.link',
    'nano.mark',
    'nano.privmsg',
    'nano.tools',
    'nano.user',
]

SETTINGS = {
    'DEBUG': True,
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
    ] + APPS,
}
if django.VERSION[:2] < (1, 6):
    SETTINGS['INSTALLED_APPS'] += ['discover_runner']
    SETTINGS['TEST_RUNNER'] = 'discover_runner.DiscoverRunner'
settings.configure(
    **SETTINGS
)

if __name__ == '__main__':
    # MUST be imported *after* settings.configure() has run!
    from django.test.utils import get_runner

    options = {
        'verbosity': 0,
    }

    TestRunner = get_runner(settings)

    test_runner = TestRunner(**options)
    failures = test_runner.run_tests(APPS)

    if failures:
        sys.exit(bool(failures))
