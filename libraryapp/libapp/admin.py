from django.contrib import admin

# Register your models here.
from models import *

class BookAdmin(admin.ModelAdmin):
	list_display = ('book_title', 'book_author')

	search_fields = ['book_title']
	search_fields = ['book_author']
	ManytoManyField = ('book_title',)

admin.site.register(Books, BookAdmin)
admin.site.register(BookUserMap)
admin.site.register(AdditionalDetails)