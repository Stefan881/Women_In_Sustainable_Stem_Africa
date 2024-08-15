from django.urls import path
from .import views 


urlpatterns = [
    path('',views.index,name='index-url'),
    path('about',views.about,name='about-url'),
    path('contact',views.contact,name='contact-url'),
    path('news',views.news,name='news-url'),
    path('support_us',views.support_us,name='support_us-url'),
    path('newsletter_subscription',views.newsletter_subscription,name='newsletter_subscription_url'),
    path('newsletters',views.newsletter,name='newsletter-url'),
]






