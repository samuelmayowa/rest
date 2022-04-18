from django.contrib import admin
from .models import Meals, MealSlideImage, About_us, Message, Contact_us, Testimonials, WhyChooseUs


# Register your models here.
class MealImageAdmin(admin.StackedInline):
    model = MealSlideImage


@admin.register(Meals)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'people',
                    'preparation_time', 'image', 'food_type', 'special_food']
    readonly_fields = ('slug',)
    list_filter = ['name', 'draft', 'special_food']

    inlines = [MealImageAdmin]


@admin.register(MealSlideImage)
class MealImageAdmin(admin.ModelAdmin):
    list_display = ['meal_name', 'slideshow']

admin.site.register(Testimonials)
admin.site.register(WhyChooseUs)
admin.site.register(Contact_us)
admin.site.register(Message)
admin.site.register(About_us)
