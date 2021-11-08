from django.db import models

# Create your models here.


class Review(models.Model):
    comment = models.TextField()
    attachment = models.FileField(upload_to='movie/attachment/review', null=True, blank=True)
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{} - Review'.format(self.movie.name)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile/images')

    def __str__(self):
        return self.first_name


class Language(models.Model):
    language = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.language


class Categories(models.Model):
    category = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(verbose_name="Movie Description")
    likes = models.IntegerField(null=True)
    watch_count = models.IntegerField(default=0, null=True)
    rate = models.PositiveIntegerField(default=0, null=True)

    # production_date = models.DateField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    poster = models.ImageField(upload_to='movie/images', null=True, blank=True)
    video = models.FileField(upload_to='movie/videos', null=True,blank=True)
    actors = models.ManyToManyField('Actor')
    language = models.ManyToManyField('Language')
    category = models.ManyToManyField('Categories')

    def __str__(self):
        return self.name
