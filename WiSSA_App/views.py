from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import NewsletterForm
from django.contrib import messages
from .models import SubscribedUsers,Post
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from tinymce.widgets import TinyMCE
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from . decorators import user_not_authenticated
from . decorators import user_is_superuser
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email =  request.POST['email']
        message = request.POST['message']

        # function to send the email
        send_mail(
            message_name,
            message,
            message_email,
            ['ondeyostephen0@gmail.com']
        )
        return render(request,'contact.html',{'message_name':message_name})
    return render(request,'contact.html')

def news(request):
    posts = Post.objects.all()
    return render(request,'news.html',{'posts':posts})

def support_us(request):
    return render(request,'support_us.html',{})

def newsletter_subscription(request):
    return render(request,'newsletter-subscription.html',{})

@user_is_superuser 
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers')
            message = form.cleaned_data.get('message')

            # Split the comma-separated string of receivers into a list
            receivers_list = [receiver.strip() for receiver in receivers.split(',')]

            mail = EmailMessage(subject, message, f"WiSSAfrica Org   <{request.user.email}>", bcc=receivers_list)
            mail.content_subtype = 'html'
            if mail.send():
                messages.success(request, "Email sent successfully")
            else:
                messages.error(request, "There was an error sending the email")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        return redirect('index-url')

    form = NewsletterForm()
    # Fetch email addresses of all subscribed users and join them into a comma-separated string
    receivers_initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    form.fields['receivers'].initial = receivers_initial
    return render(request, 'newsletter.html', {'form': form})



def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)

        if not email:
            messages.error(request,'Please enter a valid email address to subscibe to our Newsletters!...')
            return redirect('index-url')
        if get_user_model().objects.filter(email=email).first():
            messages.error(request,f'found registerd user with associated {email} email.You must login to subscribe or the unsubscibe')
            return redirect(request.META.get('HTTP_REFERER','index-url'))
        
        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request,f'{email} email address is already a subscriber')
            return redirect(request.META.get('HTTP_REFERER','index-url'))
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request,e.messages[0])
            return redirect('index-url')
        

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        messages.success(request,f'{email} email was susccessfully subscribe to our neswletter!...')
        return redirect(request.META.get('HTTP_REFERER','index-url')) 








