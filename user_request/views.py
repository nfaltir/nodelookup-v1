from django.shortcuts import render, redirect
from .forms import UserRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def user_request(request):
    if request.method == 'POST':
        form = UserRequestForm(request.POST)
        if form.is_valid():
            user_request = form.save(commit=False)
            user_request.user = request.user
            user_request.save()
            return redirect('request-success')  # Redirect to a success page or dashboard
    else:
        form = UserRequestForm()

    # Adding extra context to help users know what questions to ask
    recommended_questions = [
        "What is the growth rate of this channel over the past 6 months?",
        "What type of content receives the most engagement on this channel?",
        "How does this channel perform compared to its competitors?",
        "Which audience demographic is the most active on this channel?",
        "What are the peak times for this channel's uploads?"
    ]

    context = {
        'form': form,
        'recommended_questions': recommended_questions,
    }
    
    return render(request, 'user_request.html', context)

@login_required
def request_success(request):
    page_title = "Request Submitted!"
    context = {
        "page_title":page_title
    }
    return render(request, 'request_success.html', context)


