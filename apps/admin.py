from django.contrib import admin
from .models import New, Article, Category, Section, Company, Department, Question
from .forms import ReviewArticle, ReviewNew, ReviewCompany


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


make_visible.short_description = "Сделать видимыми"


def make_unvisible(modeladmin, request, queryset):
    queryset.update(visible=False)

make_unvisible.short_description = "Сделать невидимыми"

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sequence', 'visible',)
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_visible, make_unvisible]


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'section', 'sequence', 'visible',)
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_visible, make_unvisible]


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    form = ReviewArticle
    fields = ['title',  'category', 'text', 'file', 'published_at', ]
    list_display = ('title',  'category', 'file', 'published_at',)
    list_filter = ('category', 'published_at',)


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    form = ReviewNew
    fields = ['title', 'text', 'published_at', 'file', 'image']
    list_display = ('title', 'published_at', 'file', 'image',)
    list_filter = ('published_at',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = ReviewCompany
    list_display = ('name', 'address', 'tel', 'fax', 'email', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name',  'address', 'tel', 'fax', 'email', 'sequence', ]
    list_display = ('name', 'address', 'tel', 'fax', 'email',)
    actions = [make_visible, make_unvisible]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question',  'answer', ]
    list_display = ('question',  'answer', )



# class OrderHasDetailsInline(admin.TabularInline):
#     model = DetailOrder
#     extra = 0
