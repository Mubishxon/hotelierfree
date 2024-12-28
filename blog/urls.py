from django.urls import path
from .views import index, about, booking, contact, room, service, team, testimonial, aboutdetail, teamdetail, testimonialdetail, roomdetail, carouseldetail, servicedetail, AboutUpdateView, AboutDeleteView, AboutCreateView
urlpatterns =[
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('booking', booking, name='booking'),
    path('room', room, name='room'),
    path('service', service, name='service'),
    path('team', team, name='team'),
    path('testimonial', testimonial, name='testimonial'),
    path('aboutdetail/<slug:courses>/', aboutdetail, name='aboutdetail'),
    path('teamdetail/<int:id>/', teamdetail, name='teamdetail'),
    path('testimonialdetail/<int:id>/', testimonialdetail, name='testimonialdetail'),
    path('roomdetail/<int:id>/', roomdetail, name='roomdetail'),
    path('carouseldetail/<int:id>/', carouseldetail, name='carouseldetail'),
    path('servicedetail/<int:id>/', servicedetail, name='servicedetail'),
    path('about/edit/<slug>/', AboutUpdateView.as_view(), name='aboutUpdate'),
    path('about/delete/<slug>/', AboutDeleteView.as_view(), name='aboutDelete'),
    path('about/create', AboutCreateView.as_view(), name='aboutCreate'),
]