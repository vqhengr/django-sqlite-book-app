from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Author (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
 
    author = models.ForeignKey(Author , on_delete=models.CASCADE , null=True)
    is_bestseller = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    # image = models.ImageField(upload_to='book_images')
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    slug = models.SlugField(max_length=255, unique=True , null=False, blank=True, db_index=True)
    def __str__(self):
        return self.title
