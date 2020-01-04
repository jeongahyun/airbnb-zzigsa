from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


# @admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
# class ItemAdmin(admin.ModelAdmin):
#     """Item Admin Definition"""

#     list_display = ("name", "used_by")

#     def used_by(self, obj):
#         return obj.rooms.count()

#     pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "intro",
                    "name",
                    "description",
                    "city",
                )
            },
        ),

        ("Last Details", {"fields": ("host", "equip", "sns",)}),
    )
    list_display = (
        "name",
        "city",
        "sns",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "host__zzigsa",
        "city",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
