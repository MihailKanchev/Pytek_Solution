from django.db import models

class Category(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sub_group = models.ForeignKey("self", on_delete=models.CASCADE)
    active = models.BooleanField(default = True)

class Image(models.Model):
    img = models.ImageField(upload_to='somepath')

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    product_img = models.ForeignKey(Image, on_delete=models.CASCADE)
    img_gallery = models.ManyToManyField(Image, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=255)
    product_id = models.CharField(max_length=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    measurement_unit = models.CharField(max_length=50)
    product_price_old = models.DecimalField(decimal_places = 2)
    product_price_promo = models.DecimalField(decimal_places = 2)
    quantity_available = models.DecimalField(decimal_places = 2)
    #upload files and name them
    #product characteristics BONUS
    product_isNew = models.BooleanField(default=False)
    product_video = models.CharField(max_length=255)
    product_weight = models.DecimalField(decimal_places = 2)
    #connected products module BONUS
    #often bought together module BONUS
    meta_description = models.CharField()
    meta_keywords = models.CharField(max_length=255)
    meta_headline = models.CharField(max_length=255)
    product_active = models.BooleanField(default=True)





# class ProductDescription(models.Model):
#     product_name = models.CharField(max_length=255)
#     #img_gallery
#     #badges (new, %)
#     product_id = models.CharField(max_length=6)
#     measurement_unit = models.CharField(max_length=50)
#     #product_price bgn and eur
#     #product_price_promo
#     #promo_timer starts automatically if product is on promotion
#     #product_availability indicates  if a product is in stock
#     #product_quantity field for choosing quantity of that product
#     #product_variation list of product choices
#     #product_characteristics color, gender, age
#     product_text_description = models.CharField(max_length=255)
#     #attached_documents
#     product_weight = models.DecimalField(decimal_places = 2)
#     product_video = models.CharField(max_length=255)



