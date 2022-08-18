from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

class BooksInline(admin.TabularInline):
    model = Book
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    list_display = ("id","book","status","borrower","due_back")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
