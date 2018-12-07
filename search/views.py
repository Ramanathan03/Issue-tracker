from django.shortcuts import render
from tickets.models import add_tickets_form
# Create your views here.

def do_search(request):
    issue = add_tickets_form.objects.filter(title__icontains=request.GET['q'])
    return render(request, 'search.html', {'issue':issue, "query": request.GET.get('q', None)})
