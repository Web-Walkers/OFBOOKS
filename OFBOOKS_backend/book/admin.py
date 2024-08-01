from django.contrib import admin

from .models import Book, \
                    Publishing_Company, \
                    Author, \
                    Interpreter, \
                    Subject, \
                    Literature, \
                    Genre, \
                    Achievement

from django.utils.timesince import timesince

admin.site.register(Achievement)

@admin.register(Publishing_Company)
class PublishingCompanyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')

@admin.register(Interpreter)
class InterpreterAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')
    

@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'item_count')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'genres')
    list_display = ('__str__', 
                    'author', 
                    'publisher',
                    'subject',
                    'readable_credit_',  
                    'created_at_formatted')
    search_fields = ('id', 'name',)
    
    exclude = ('created_by', )

    def readable_credit_(self, obj):
        return obj.readable_credit()
    readable_credit_.short_description = 'قیمت'

    def created_at_formatted(self, obj):
        return timesince(obj.created_at).translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')) + " قبل"
    created_at_formatted.short_description = 'بارگذاری شده در'

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