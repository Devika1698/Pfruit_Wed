from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255)
    folder_image = models.ImageField(upload_to='folder_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class WeddingImage(models.Model):
    image = models.ImageField(upload_to='images/')
    event_type = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, default=1)