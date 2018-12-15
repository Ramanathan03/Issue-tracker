from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePayement
from tickets.forms import ticketsForm, CommentForm
from tickets.models import add_tickets_form, Comment_form
from django.conf import settings
from accounts.views import user_login, index 
from django.utils import timezone
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    forms = ticketsForm(request.POST)
    High = add_tickets_form()
    if request.method == "POST":
                    
        try:
                customer = stripe.Charge.create(
                    amount = 200,
                    currency = "EUR",
                    description = "We will fix your problem in few hours" and request.user.email,
                    source = request.POST.get('stripeToken'),
                    )
                print(customer.amount)
        except stripe.error.CardError:
                messages.error(request,"Your card was declined")
            
        if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect('confrim') 
                
        else:
                messages.error(request, "Unable to take payment")
                return redirect(index)
                
        #else:
         #   return redirect(index)
        
            
    else:
        payment_form = MakePayement()
        
        
    return render(request, 'checkout.html', {'payment_form':payment_form, 'publishable':settings.STRIPE_SECRET})
            