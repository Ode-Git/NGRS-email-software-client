#!/usr/bin/env python3

#  Copyright (c) 2020 openKirkes, developed by Otso Kurkela

import os
import sys
import random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openKirkes.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
       
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
