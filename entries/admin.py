# Register your models here.
# entries/admin.py
from django.contrib import admin
from .models import Entry

# admin.site.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    # Adding filters for 'status' and 'date_created'
    list_filter = ('status', 'date_created')

    # Optionally, you can also customize the list display
    list_display = ('title', 'status', 'date_created')
    search_fields = ('title', 'content')

# Register the Entry model with the customized EntryAdmin
admin.site.register(Entry, EntryAdmin)