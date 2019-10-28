#!/usr/bin/env python
import os
import sys
import pydevd_pycharm

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

    from django.core.management import execute_from_command_line

    # pydevd_pycharm.settrace('localhost', port=8788, stdoutToServer = True, stderrToServer = True)

    execute_from_command_line(sys.argv)
