from django.contrib import admin
from .forms import KonUserCreationForm, KonUserChangeForm
# Register your models here.
from .models import KonUser, AssetPackage, Lesson,Category,Book
from django.utils.html import format_html
@admin.register(KonUser)
class KonUserAdmin(admin.ModelAdmin):
    add_form = KonUserCreationForm
    form = KonUserChangeForm
    model = KonUser
    list_display = ['email', 'username',]

@admin.register(AssetPackage)
class AssetPackageAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass