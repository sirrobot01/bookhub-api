from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

# Create your models here.


User = get_user_model()


class ShelvesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ShelvesModel, self).save()


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CategoryModel, self).save()


class BookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelf = models.ForeignKey(ShelvesModel, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BookModel, self).save()
