from django.contrib import admin

from .models import Crew, Owner, Sacco, Supervisor, Vehicle

# Register your models here.
admin.site.register(Sacco)
admin.site.register(Supervisor)
admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(Crew)
