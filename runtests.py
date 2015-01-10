#!/usr/bin/env python

from __future__ import unicode_literals

import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'nano.tests.settings'
sys.path.append('.')

from django.conf import settings
from django.test.utils import get_runner

if __name__ == '__main__':
    try: # Django 1.7+
        from django import setup
        setup()
    except ImportError:
        pass

    options = {
        'verbosity': 0,
    }

    TestRunner = get_runner(settings)

    test_runner = TestRunner(**options)
    failures = test_runner.run_tests(settings.APPS)

    if failures:
        sys.exit(bool(failures))
