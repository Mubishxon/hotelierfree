from django.contrib import admin
from .models import Carousel, About, Team, Testimonial, Service, Room, Contact, Newsletter
# Register your models here.
admin.site.register(Carousel)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(Room)
admin.site.register(Contact)
admin.site.register(Newsletter)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

