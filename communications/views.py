from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create the message object but do not save it yet
            new_message = form.save(commit=False)
            new_message.sender = request.user  # Set the sender to the current logged-in user
            new_message.save()  # Save the message without a recipient (staff will access in admin)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('inbox')  # Redirect to inbox or another page
    else:
        form = MessageForm()

    context = {
        'form': form,
        'page_title': 'Send Message'
    }

    return render(request, 'send_message.html', context)



def inbox(request):
    page_title = "User Inbox"
    # Fetch messages where the current logged-in user is the sender
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')

    context = {
        "page_title": page_title,
        "messages": messages
    }

    return render(request, 'inbox.html', context)