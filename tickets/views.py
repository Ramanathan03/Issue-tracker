from django.shortcuts import render, redirect, reverse

# Create your views here.
def add_tickets(request):
    return render(request,'add_tickets.html')