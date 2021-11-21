from django.contrib import admin
from .models import Article, Comment

# Register your models here.

"""
admin.site.register(Article)
"""

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]   # admin panelinde makale listesinde diğer bilgilerin de gösterilmesi
    list_display_links = ["title","created_date"]   # İçeriğe erişmek için link ekleme
    search_fields = ["title"]  # Title bilgisine göre arama özelliği
    list_filter = ["created_date"]   # Makale oluşturulma tarihi süzgeci
    # list_filter = ["title"]   # Başlığa göre fitreleme
    class Meta:
        model = Article

