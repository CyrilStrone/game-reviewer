from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Category, Genre, Game, GameShots, Developer, Rating, RatingStar, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget 


class GameAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	"""Категории"""
	list_display = ("id", "name", "url")
	list_display_links = ("name",)

class ReviwInline(admin.TabularInline):
	model = Reviews
	extra = 1
	readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	"""Категории"""
	list_display = ("id", "name", "url")
	list_display_links = ("name",)

class GameShotsInline(admin.TabularInline):
	"""Скриншоты в окнах игр"""
	model = GameShots
	extra = 1
	readonly_fields = ("get_image",)
	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="110" height="110"')
	get_image.short_description = "Скриншот"

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	"""Игра"""
	list_display = ("title", "url", "get_image", "draft",)
	readonly_fields = ("get_image",)
	list_display_links = ("title",)
	list_filter = ("draft", "year",)
	search_fields = ("title", )
	inlines = [GameShotsInline, ReviwInline]
	save_on_top = True
	save_as = True
	list_editable = ("draft",)
	actions = ["publish", "unpublish"]
	form = GameAdminForm
	
	def get_image(self, obj):
		return mark_safe(f'<img src={obj.poster.url} width="120" height="120"')

	get_image.short_description = "Изображение"

	def unpublish(self, request, queryset):
		"""Снять с публикации"""
		row_update = queryset.update(draft=True)
		if row_update == 1:
			message_bit = "1 запись была обновлена"
		else:
			message_bit = f"{row_update} записей были обновлены"
		self.message_user(request, f"{message_bit}")

	def publish(self, request, queryset):
		"""Опубликовать"""
		row_update = queryset.update(draft=False)
		if row_update == 1:
			message_bit = "1 запись была обновлена"
		else:
			message_bit = f"{row_update} записей были обновлены"
		self.message_user(request, f"{message_bit}")

	publish.short_description = "Опубликовать"
	publish.allowed_permissions = ('change',)

	unpublish.short_description = "Снять с публикации"
	unpublish.allowed_permissions = ('change',)

	fieldsets = (
	    (None, {
	        "fields": ("title",)
	    }),
	        (None, {
	            "fields": ("description", ("poster", "get_image",),)
	        }),
	        (None, {
	            "fields": (("date", "year",),)
	        }),
	        (None, {
	            "fields": (("developer", "publisher", "genre", "category"),)
	        }),
	        (None, {
	            "fields": ("trailer",)
	        }),
	        ("Options", {
	            "fields": (("url", "draft",),)
	        }),
	    )




@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
	"""ReviewAdmin"""
	list_display = ("name", "email", "parent", "game", "id")
	readonly_fields = ("name", "email")

@admin.register(GameShots)
class GameShotsAdmin(admin.ModelAdmin):
	"""ReviewAdmin"""
	list_display = ("title", "game","get_image",)
	readonly_fields = ("get_image",)
	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="70" height="70"')
	get_image.short_description = "Изображение"



@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
	"""ReviewAdmin"""
	list_display = ("name", "get_image",)
	readonly_fields = ("get_image",)
	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="70" height="70"')
	get_image.short_description = "Изображение"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	"""ReviewAdmin"""
	list_display = ("game", "star", "ip", "user")


		
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Genre)
#admin.site.register(Game)
#admin.site.register(GameShots)
#admin.site.register(Developer)
#admin.site.register(Rating)
admin.site.register(RatingStar)
#admin.site.register(Reviews)
