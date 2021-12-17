from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from django.db.models.deletion import CASCADE


class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=50, blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    IMAGE_MAXSIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAXSIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Ticket(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField()
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)


class Review(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    titleR = models.CharField(max_length=128, verbose_name='titre')
    comment = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
