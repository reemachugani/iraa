from django.contrib import admin
from .models import Art, Art_Category, Art_Url

class Art_UrlInline(admin.TabularInline):
    model = Art_Url

class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'art_type',)
    list_filter = ('art_type__category',)
    inlines = [
        Art_UrlInline,
    ]

    class Media:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js',)

class Art_CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

admin.site.register(Art, ArtAdmin)
admin.site.register(Art_Category, Art_CategoryAdmin)


