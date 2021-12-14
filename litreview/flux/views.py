import datetime
from django.forms import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from itertools import chain
from django.db.models import Value, CharField
from .models import Ticket


@login_required
def flux(request):
    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = models.Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )
    return render(request, 'flux/flux.html', context={'posts': posts})


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

    return render(request, 'flux/create_ticket.html', context={'form': form})


@login_required
def create_review(request):
    formticket = forms.TicketForm()
    formreview = forms.ReviewForm()
    if request.method == 'POST':
        formticket = forms.TicketForm(request.POST, request.FILES)
        formreview = forms.ReviewForm(request.POST)
        if all([formticket.is_valid(), formreview.is_valid()]):
            ticket = formticket.save(commit=False)
            ticket.uploader = request.user
            ticket.reviewed = True
            ticket.save()
            review = formreview.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')

    context = {'formticket': formticket, 'formreview': formreview}

    return render(request, 'flux/create_review.html', context=context)


@login_required
def review_to_ticket(request, ticket_id):
    form = forms.ReviewForm()
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            ticket.reviewed = True
            ticket.save()
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')

    context = {'form': form, 'ticket': ticket}
    return render(request, 'flux/review_to_ticket.html', context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('flux')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'flux/edit_ticket.html', context=context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('flux')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'flux/edit_review.html', context=context)


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(uploader=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = models.Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )
    return render(request, 'flux/posts.html', context={'posts': posts})
