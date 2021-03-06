# Generated by Django 3.2.4 on 2021-08-27 22:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_ckeditor_5.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_content', models.TextField(help_text='inspiration behind the company', max_length=600)),
                ('origin_image', models.ImageField(help_text='image of your choice', upload_to='restaurant/meals/about')),
                ('why_we_are_best_content', models.TextField(help_text='reason we are the best', max_length=270)),
                ('why_we_are_best_image', models.ImageField(help_text='why we best', upload_to='restaurant/meals/about')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': ' About Us',
            },
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='NG')),
                ('content', models.TextField(help_text='any unique information you want to share', max_length=150)),
            ],
            options={
                'verbose_name': 'Contact us',
                'verbose_name_plural': 'Contact us',
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('people', models.IntegerField()),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, error_messages={'name': {'max_length': 'The price you want to sell the product'}}, help_text='Price you which to sell the product', max_digits=10, verbose_name='Price')),
                ('preparation_time', models.IntegerField(error_messages={'name': {'max_length': 'write only digit'}}, help_text='The total wait time(only digit)')),
                ('image', models.ImageField(blank=True, upload_to='restaurant/meals')),
                ('food_type', models.CharField(choices=[('local_dishes', 'Local Dishes'), ('fast_food', 'Fast Food'), ('pizza', 'Pizza'), ('burger', 'Burger'), ('soft drink', 'Soft Drink'), ('others', 'Others')], max_length=50, null=True)),
                ('published_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 27, 22, 0, 54, 545454, tzinfo=utc))),
                ('special_food', models.BooleanField(default=False, help_text='Click to make product show in the special category section')),
                ('banner', models.BooleanField(default=False, help_text='You should have a banner')),
                ('hot_menu', models.BooleanField(default=False, help_text="This will show the hot product's title in the footer section")),
                ('draft', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
                'ordering': ['-published_date'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('your_email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=280)),
                ('name', models.CharField(default='Company Name', max_length=50)),
                ('office_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='restaurant/meal/testimonials')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='restaurant/meal/about')),
            ],
            options={
                'verbose_name': 'Why Choose us',
                'verbose_name_plural': 'Why Choose us',
            },
        ),
        migrations.CreateModel(
            name='MealSlideImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideshow', models.FileField(upload_to='restaurant/meals/slideshow')),
                ('meal_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='meals.meals')),
            ],
        ),
    ]
