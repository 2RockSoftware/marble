#!/usr/bin/env python
import os
import sys

from marble import load_env

load_env.load_env()

if __name__ == "__main__":
    if 'DATABASE_URL' in os.environ:
        # Dokku or similar
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marble.settings.deploy")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marble.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
