from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

User = get_user_model()


class Menu(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=255)
    order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ('order',)


class HomePage(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    background = models.ImageField(upload_to="background/")

    def __str__(self):
        return "{}".format(self.title)

    def preview_image(self):
        return mark_safe(
            "<img src='{}' style='width:300px' />".format(
                self.background.url
            )
        )

class Article(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(null=True, blank=True, max_length=255)
    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               on_delete=models.DO_NOTHING)
    text = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/",null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)

class Footer(models.Model):
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    # copyright
    copyright = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.copyright)