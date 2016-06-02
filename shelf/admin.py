from django.contrib import admin
from .models import Author, Book, Publisher

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name']
    ordering = ['last_name'] # jesli z minusem to malejaco

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','author','isbn','publisher']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register([Publisher])


