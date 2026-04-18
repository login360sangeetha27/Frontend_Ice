import django
from django.template.context import BaseContext
import inspect
print('Django', django.get_version())
print(inspect.getsource(BaseContext.__copy__))
