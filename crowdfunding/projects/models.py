from django.contrib.auth import get_user_model
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='Project'
    )
    # category = models.CategoryField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()



class Project_Product(BaseModel):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='project_product'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='product'
    )
    purchased_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_project_product'
    )
    purchased_date = models.DateTimeField()
    anonymous = models.BooleanField()
    comment = models.CharField(max_length=200)

class Category(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()


class Product(BaseModel):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    image = models.CharField(max_length=200)
    gtin = models.CharField(max_length=200)
