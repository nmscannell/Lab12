from django.contrib import admin
from user.models import user,gift,usergift
# Register your models here.

admin.site.register(usergift)
admin.site.register(user)
admin.site.register(gift)

