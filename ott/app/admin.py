from django.contrib import admin
from .models import Movie, Customer, Subscription

# Register your models here.
admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(Subscription)




class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'duration', 'created')
    search_fields = ('title', 'genre', 'director')
    list_filter = ('genre', 'director')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email', 'Mobile', 'Plan', 'End_date')
    search_fields = ('FirstName', 'LastName', 'Email')
    list_filter = ('Plan', 'End_date')
