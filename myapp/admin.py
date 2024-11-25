from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Login_model)
admin.site.register(User_model)
admin.site.register(Diver_model)
admin.site.register(Complaint_model)
admin.site.register(Feedback_model)