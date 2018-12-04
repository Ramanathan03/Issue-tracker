from django.shortcuts import render, redirect, reverse,get_object_or_404
from tickets.forms import ticketsForm, CommentForm
from .models import add_tickets_form, Comment_form
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import now
from accounts.views import user_login, index
from checkout.views import checkout
from django.contrib.auth.models import User
# Create your views here.
@login_required
def add_tickets(request):
    Priority = 'HIGH'
    if request.method == "POST":
        forms = ticketsForm(request.POST)
        if forms.is_valid() and 'HIGH' in request.POST['priority'] :
             request.session['priority'] = forms.cleaned_data['priority']
             request.session['title']       = forms.cleaned_data['title']
             request.session['description'] = forms.cleaned_data['description']
             request.session['type'] = forms.cleaned_data['type']
             return redirect(checkout)
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
 
@login_required
def confrim(request):
    title       = request.session['title']
    description = request.session['description']
    priority    = request.session['priority']
    type = request.session['type']
    data = {'title': title,
            'description': description,
            'priority': priority,
            'type': type
    }
    if request.GET & ticketsForm.base_fields.keys():
        form = ticketsForm(request.GET)
    else:
        form = ticketsForm(data, request.POST or None)

    if request.method == 'POST':
        # if form is valid - create ticket
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, "You have successfully created and paid for a new feature Ticket.")
            return redirect(reverse('index'))
        else:
            messages.success(request, "Sorry, something went wrong. Please try again later.")
            return redirect(reverse('index'))

    return render(request, 'confrim.html', {'form': form})           

            