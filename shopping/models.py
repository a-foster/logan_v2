from django.db import models

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category_code = models.ForeignKey(ProductCategory, to_field="id", db_column="category_name", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_added = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product_name