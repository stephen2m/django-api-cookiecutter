import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, project_slug):
    print('ERROR: %s is not a valid Python module name!' % project_slug)
    sys.exit(1)