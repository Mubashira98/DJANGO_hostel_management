from django.contrib import admin

from APP import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Student_register)
admin.site.register(models.Parent_register)
admin.site.register(models.Hostel)
admin.site.register(models.Food)
admin.site.register(models.Notification)
admin.site.register(models.Attendance)
admin.site.register(models.Complaint)
admin.site.register(models.Payment)
admin.site.register(models.Review)
admin.site.register(models.Staff)
admin.site.register(models.Room_booking)

