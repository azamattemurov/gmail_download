from django.contrib import admin
from bookapp.models import BookModel

# Register your models here.
@admin.register(BookModel)
class BookAdminModel(admin.ModelAdmin):
    list_display = ['author', 'name', 'pages','created_at']
    search_fields = ['name']
    list_filter = ['created_at','author']