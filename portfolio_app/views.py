from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        sender_name = request.POST['sender-name']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        sender_email = request.POST['sender-email']
        
        
    #Send email
        send_mail(
            sender_name + " : " + message_subject, #subject
            message, #message
            sender_email, #from email
            ['jpbongiovanni@gmail.com'], # to email
            fail_silently=False,
        )

        return render(request, 'index.html', {'sender_name': sender_name})
    
    else:
        return render(request, 'index.html', {})