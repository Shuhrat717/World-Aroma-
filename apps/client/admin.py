from django.contrib import admin
from apps.client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'email', 'created_at')
    list_display_links = ('id', 'fullname', 'phone', 'email', )


admin.site.register(Client, ClientAdmin)
