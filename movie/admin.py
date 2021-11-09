from django.contrib import admin
from .models import Movie, Actor, Review, Language, Categories


class InlineActors(admin.TabularInline):
    model = Movie.actors.through
    extra = 1


class InlineCategory(admin.TabularInline):
    model = Movie.category.through
    extra = 1


class InlineLanguage(admin.TabularInline):
    model = Movie.language.through
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'likes', 'rate', 'watch_count', 'custom_list',  'creation_date',)
    inlines = [InlineActors, InlineCategory, InlineLanguage]

    def custom_list(self, obj):
        if obj.likes and obj.watch_count:
            total_rate = 100 * (obj.likes/obj.watch_count)
            return '{} %'.format(round(total_rate))
        return 0

    custom_list.short_description='Movie Rate'

    fieldsets = (
        ['Main Section', {'fields': ['name', 'description']}],
        ['Statistics Section', {'fields': ['likes', 'watch_count', 'rate']}],
        ['Attachment Section', {'fields': ['poster', 'video']}],
        # ['Related Information Section', {'fields': ['categories']}],
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Language)
admin.site.register(Categories)
