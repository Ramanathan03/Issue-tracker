from django.shortcuts import render, redirect, reverse,get_object_or_404
from tickets.forms import ticketsForm, CommentForm
from .models import add_tickets_form, Comment_form
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.utils import timezone
from accounts.views import user_login, index
from django.contrib.auth.models import User
# Create your views here.

def add_tickets(request):
    Priority = 'HIGH'
    if request.method == "POST":
        forms = ticketsForm(request.POST)
        if forms.is_valid() and 'HIGH' in request.POST['priority'] :
             request.session['priority'] = forms.cleaned_data['priority']
             return redirect(add_tickets)
        if forms.is_valid():
            issue_data = forms.cleaned_data
            add_issue = add_tickets_form.objects.create(
                title = issue_data['title'],
                author = request.user,
                description = issue_data['description'],
                priority = issue_data['priority'],
                type = issue_data['type'],
                )
            
            return redirect(index)
    else:
        forms = ticketsForm()
    return render(request, 'add_tickets.html',{'forms':forms})

def show_tickets(request, pk):
    ticket = get_object_or_404(add_tickets_form , pk=pk)
    ticket.views += 1
    ticket.save()
    print(ticket)
    #ticket_id = request.POST.get('ticket_id', None)
    #issue = add_tickets_form.objects.filter(id=ticket_id).first()
    if request.method == "POST":
       commentbox = CommentForm(request.POST)
       if commentbox.is_valid(): 
            comment_data = commentbox.cleaned_data
            add_issue = Comment_form.objects.create(
                comment = comment_data['comment'],
                user = request.user,
                ticket = get_object_or_404(add_tickets_form, pk=pk)
                )
            return redirect(show_tickets,ticket.pk)
       print(commentbox)
    else:
        commentbox = CommentForm()
    
    comment = Comment_form.objects.all()
    return render(request, 'show_tickets.html', {'ticket':ticket, 'commentbox':commentbox, 'comment':comment})
            

            