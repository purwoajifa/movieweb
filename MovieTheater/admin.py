from django.contrib import admin
from . models import *

admin.site.register(cinema)
admin.site.register(movie)
admin.site.register(showing)
admin.site.register(theater)
admin.site.register(ticket)