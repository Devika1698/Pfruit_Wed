from django.contrib import admin
from .models import WeddingImage, Folder

@admin.register(WeddingImage)
class WeddingImageAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'upload_date', 'folder')

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder_image')
