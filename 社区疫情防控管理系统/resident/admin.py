from django.contrib import admin
from resident import models

# Register your models here.
admin.site.register(models.UserProfil)
admin.site.register(models.DailyRepords)
admin.site.register(models.GetInto)
admin.site.register(models.GetOut)