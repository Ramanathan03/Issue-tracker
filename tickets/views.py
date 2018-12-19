from django.shortcuts import render, redirect, reverse,get_object_or_404
from tickets.forms import ticketsForm, CommentForm
from .models import add_tickets_form, Comment_form
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import RedirectView
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
    
    #comment = Comment_form.objects.all()
    #like = like_posts.objects.all()
    
    return render(request, 'show_tickets.html', {'ticket':ticket, 'commentbox':commentbox})
    
@login_required
def edit_tickets(request,id):
    ticket =get_object_or_404(add_tickets_form,pk=id)
    if request.method == "POST":
        form = ticketsForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect(show_tickets, ticket.id)
    else:
        form = ticketsForm(instance=ticket)
    return render(request,"edit_tickets.html",{'form':form})
 
@login_required
def edit_comments(request,id):
    comment = get_object_or_404(Comment_form,pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = CommentForm(instance=comment)
    return render(request,"edit_comments.html",{'form':form})

@login_required
def delete_ticket(request,id):
    ticket = get_object_or_404(add_tickets_form,pk=id)
    if request.method == "POST":
        ticket.delete()
        return redirect(add_tickets)
    return render(request,"cofirm-ticket-delete.html",{'ticket':ticket})
        


@login_required
def delete_comments(request, id):
    comments = get_object_or_404(Comment_form, pk=id)
    if request.method == "POST":
       comments.delete()
       return redirect(index)
    return render(request,"confirm_delete.html",{'comments':comments})


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

@login_required
def upvote_tickets(request,id):
    ticket = get_object_or_404(add_tickets_form, pk=id)
    if ticket.like_and_dislike == 2  :
          ticket.like_and_dislike -= 1
    else:
        ticket.like_and_dislike += 1
        ticket.save()
    return redirect(show_tickets, ticket.id)

@login_required
def down_vote(request,id):
    ticket = get_object_or_404(add_tickets_form, pk=id)
    if ticket.like_and_dislike == 0:
        ticket.like_and_dislike = 0
        ticket.save()
    else:
     ticket.like_and_dislike -= 1
     ticket.save()
    return redirect(show_tickets, ticket.id)

    
            