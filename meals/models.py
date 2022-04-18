from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField

# the following filters the front and other section's content accordingly

food_type = (
    ('Local Lishes', 'Local Dishes'),
    ('Fast Food', 'Fast Food'),
    ('Pizza', 'Pizza'),
    ('Burger', 'Burger'),
    ('Soft Drink', 'Soft Drink'),
    ('Others', 'Others')
)


# Create your models here.

class Meals(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    people = models.IntegerField()
    selling_price = models.DecimalField(
        verbose_name=("Price"),
        help_text=("Price you which to sell the product"),
        error_messages={
            "name": {
                "max_length": ("The price you want to sell the product"),
            },
        },
        max_digits=10,
        decimal_places=2, default=0
    )
    preparation_time = models.IntegerField(help_text=("Time the food is expected to be ready in minutes(only digits)"),
                                           error_messages={
        "name": {
            "max_length": ("write only digit"),
        },
    },)
    image = models.ImageField(upload_to='restaurant/meals', blank=True)

    food_type = models.CharField(null=True, max_length=50, choices=food_type, default='Others')
    published_date = models.DateTimeField(timezone.now(), auto_now_add=True)
    special_food = models.BooleanField(default=False, help_text=(
        "Click to make product show in the special category section"))
    banner = models.BooleanField(default=False, help_text=(
        "You should have a banner"))
    hot_menu = models.BooleanField(default=False, help_text=(
        "This will show the hot product's title in the footer section"))
    draft = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'
        ordering = ['-published_date']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    # the following makes sure that slug is included
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    def summary(self):
        return self.description[:99]


class MealSlideImage(models.Model):
    meal_name = models.ForeignKey(
        Meals, default=None, on_delete=models.CASCADE, related_name='meals')
    slideshow = models.FileField(
        upload_to='restaurant/meals/slideshow')

    def __str__(self):
        return self.meal_name.name


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='restaurant/meal/about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Why Choose us'
        verbose_name_plural = 'Why Choose us'


class Testimonials(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=280)
    name = models.CharField(max_length=50, default='Company Name')
    office_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restaurant/meal/testimonials')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class About_us(models.Model):
    origin_content = models.TextField(
        max_length=600, help_text='inspiration behind the company')
    origin_image = models.ImageField(
        upload_to='restaurant/meals/about', help_text='image of your choice')
    why_we_are_best_content = models.TextField(
        max_length=270, help_text='reason we are the best')
    why_we_are_best_image = models.ImageField(
        upload_to='restaurant/meals/about', help_text='why we best')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = ' About Us'

    def __str__(self):
        return 'About us Content'


class Contact_us(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = PhoneNumberField(region='NG')
    content = models.TextField(help_text=(
        "any unique information you want to share"), max_length=150)

    class Meta:
        verbose_name_plural = 'Contact us'
        verbose_name = 'Contact us'

    def __str__(self):
        return self.address


class Message(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return 'Message from {}'.format(self.your_name.upper())
