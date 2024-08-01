from django.contrib import admin

from .models import Blog, Paragraph, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count', 'is_trend')
    list_editable = ['is_trend']
    def item_count(self, obj):
        return obj.blogs.count()
    item_count.short_description = 'تعداد استفاده'

@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'blog')
    ordering = ['blog', 'created_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_display = ('__str__', 'created_by', 'created_at_formatted')
    exclude = ('created_by', )

    def save_model(self, request, obj, form, change): 
        obj.created_by = request.user
        obj.save()

    # def save_formset(self, request, form, formset, change): 
    #     if formset.model == Comment:
    #         instances = formset.save(commit=False)
    #         for instance in instances:
    #             instance.user = request.user
    #             instance.save()
    #     else:
    #         formset.save()
