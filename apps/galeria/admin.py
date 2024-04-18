from django.contrib import admin
from apps.galeria.models import Fotografia

class DisplayFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "legenda")
    list_display_links = ("id", "nome")
    list_filter = ("categoria","usuario")
    # list_editable = ('publicada',)
    list_per_page = 10
    

admin.site.register(Fotografia, DisplayFotografias)