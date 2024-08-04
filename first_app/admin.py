from django.contrib import admin
from first_app.models import *


admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)