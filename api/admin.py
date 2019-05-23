from django.contrib import admin
from .models import Users, NormalUSer, Books
# Register your models here.


admin.site.register(Books)
admin.site.register(Users)
admin.site.register(NormalUSer)
