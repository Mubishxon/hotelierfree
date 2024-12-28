from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Carousel, About, Team, Testimonial, Service, Room
from .forms import NewsletterForm, ContactForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.
class AboutUpdateView(UpdateView):
    model = About
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'AboutEdit.html'

class AboutDeleteView(DeleteView):
    model = About
    template_name = 'AboutDelete.html'
    success_url = reverse_lazy('index')

class AboutCreateView(CreateView):
    model =About
    template_name = 'AboutCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Aboutdetail(request, about):
    about = get_object_or_404(About, slug=about)
    context = {
        'about': about
    }
    return render(request, 'aboutDetailView', context=context)

def index(request):
    carousel = Carousel.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    service = Service.objects.all()
    room = Room.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "carousel": carousel,
        "about": about,
        "team": team,
        "testimonial": testimonial,
        "service": service,
        "room": room,
        "contact": contact,
        "newsletter": newsletter
    }
    return render(request, 'index.html', context=context)


def room(request):
    room = Room.objects.all()
    context = {
        'room': room
    }
    return render(request, 'room.html', context=context)


def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)

def newsletter(request):
    newsletter =NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "newsletter": newsletter
    }
    return render(request, 'newsletter.html', context=context)

def team(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'team.html', context=context)



def testimonial(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'testimonial.html', context=context)


def about(request):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'about.html', context=context)


def service(request):
    service = Service.objects.all()
    context = {
        'service': service
    }
    return render(request, 'service.html', context=context)


def booking(request):
    return render(request, 'booking.html', context={})

def carouseldetail(request, id):
    carousel = Carousel.objects.get(id=id)
    context = {
        'x': carousel
    }
    return render(request, 'carouseldetail.html', context=context)

def aboutdetail(request, id):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'aboutdetail.html', context=context)

def teamdetail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'x': team
    }
    return render(request, 'teamdetail.html', context=context)

def testimonialdetail(request, id):
    testimonial = Testimonial.objects.get(id=id)
    context = {
        'x': testimonial
    }
    return render(request, 'testimonialdetail.html', context=context)

def roomdetail(request, id):
    room = Room.objects.get(id=id)
    context = {
        'x': room
    }
    return render(request, 'roomdetail.html', context=context)

def servicedetail(request, id):
    service = Service.objects.get(id=id)
    context = {
        'x': service
    }
    return render(request, 'servicedetail.html', context=context)