from django.db import models

# Create your models here.

class ImageCategory(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name


class ImageSearch(models.Model):
    img_name = models.CharField(max_length=120)
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.img_name
