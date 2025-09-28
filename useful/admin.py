from django.contrib import admin

from useful.models import Article, Document

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]
    list_display = ('title','choice','slug',)

class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]
    list_display = ('title', 'slug',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Document, DocumentAdmin)
