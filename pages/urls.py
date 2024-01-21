# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("education/", views.education, name='education'),
    path("health/", views.health, name='health'),
    path("empowerment/", views.empowerment, name='empowerment'),
    path("school/", views.school, name='school'),
    path("volunteers/", views.volunteers, name='volunteers'),
    path("work/", views.work, name='work'),
    path("contact/", views.contact, name='contact'),
    path("faq/", views.faq, name='faq'),

]