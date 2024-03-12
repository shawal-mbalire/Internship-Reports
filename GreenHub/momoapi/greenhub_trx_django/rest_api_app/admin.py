from django.contrib import admin
from rest_api_app.models import MyUser,Transfer,Collection

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Transfer)
admin.site.register(Collection)