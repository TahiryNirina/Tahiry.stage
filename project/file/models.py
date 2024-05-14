from django.db import models

# Create your models here.


class File(models.Model):
    caption = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.caption