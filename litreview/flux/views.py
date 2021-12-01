from django.forms import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


@login_required
def flux(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets':tickets})


@login_required
def create_ticket(request):
    form = forms.TicketForm
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect('flux')
    
    return render(request, 'flux/create_ticket.html', context={'form':form})

@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.uploader = request.user
            review.save()
            return redirect('flux')

    return render(request, 'flux/create_review.html', context={'form':form})