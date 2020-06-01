from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'DASHBOARD ADMIN'
admin.site.site_title = 'DOSHISAMAJ'
admin.site.site_url = 'http://127.0.0.1:8000/AdminDashbord/'
admin.site.index_title = 'DOSHISAMAJ ADMINISTRATION'
admin.empty_value_display = '**Empty**'

admin.site.register(NewsAndEventsBlog)
