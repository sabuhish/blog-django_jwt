from django.contrib import admin
from .models import Menu, HomePage, Article, Footer

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "order", "status")

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    readonly_fields = ('preview_image',)
    list_display = ('preview_image', 'title', 'sub_title')

admin.site.register(Article)
admin.site.register(Footer)