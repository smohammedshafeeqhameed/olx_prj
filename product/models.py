from django.db import models
from user.models import OlxUser



class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField("Product", through="ProductCategory")
    category_state = models.BooleanField(default=True, verbose_name="Availability")

    def __str__(self):
        """Returns category name"""
        return self.category_name

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="product_pic")
    added_by = models.ForeignKey(OlxUser, on_delete=models.CASCADE)
    description = models.TextField()
    categories = models.ManyToManyField("Category", through="ProductCategory")
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    width = models.FloatField(null=True, default=10)
    height = models.FloatField(null=True, default=12)
    weight = models.FloatField(null=True, default=11)
    product_status = models.BooleanField(default=True)

    def __str__(self):
        """String representation of the Product object will return the name of current product object"""
        return self.name


# The through table of many to many relationship between Product and Category
class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " (" + self.category.category_name + ")"
    

class Order(models.Model):
    """Creating a order after a customer successfully checks out."""

    customer = models.ForeignKey(OlxUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    house_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    mode_of_payment = models.CharField(default="COD", max_length=255)
    total = models.FloatField()
    status = models.BooleanField(default=False)


class OrderProduct(models.Model):
    """An order can have multiple products associated with it, this model stores just that."""

    order = models.ForeignKey(
        Order, related_name="orderproduct", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.FloatField(max_length=200)