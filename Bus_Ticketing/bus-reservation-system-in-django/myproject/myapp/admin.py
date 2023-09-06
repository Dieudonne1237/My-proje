from django.contrib import admin
from .models import Bus, User, Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['email', 'name', 'userid', 'busid', 'bus_name', 'source', 'dest', 'nos', 'price', 'date', 'time', 'status']


class BusAdmin(admin.ModelAdmin):
    list_display=['bus_name', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time',]


class UserAdmin(admin.ModelAdmin):
    list_display=['user_id', 'email', 'name', 'password']

admin.site.register(Bus, BusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)


