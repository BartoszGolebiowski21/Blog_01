from django.db import models
from datetime import date
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=300)
    author = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.date}, from post: {self.post}"