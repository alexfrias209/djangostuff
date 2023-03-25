from django.contrib import admin

# Register your models here.
from .models import Room
from .models import UserProfile,Account,MultipleImage

admin.site.register(Room)
admin.site.register(UserProfile)
admin.site.register(Account)
admin.site.register(MultipleImage)