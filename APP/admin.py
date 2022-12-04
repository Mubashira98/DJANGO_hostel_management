from django.contrib import admin

from APP import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Student_register)
admin.site.register(models.Parent_register)