from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')

@admin.register(Product)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'readable_credit', 'created_at_formatted')
    search_fields = ('id', 'name',)
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
