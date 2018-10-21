#!/usr/bin/env python

from __future__ import unicode_literals

import sys
import os

from django.conf import settings
from django.test.utils import get_runner

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    sys.path.append('.')

    from django import setup
    setup()

    options = {
        'verbosity': 2,
        'top_level': '.',
    }

    TestRunner = get_runner(settings)

    test_runner = TestRunner(**options)
    failures = test_runner.run_tests(settings.APPS)

    if failures:
        sys.exit(bool(failures))
