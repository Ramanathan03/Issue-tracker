from django import forms
from tickets.models import add_tickets_form, Comment_form

class ticketsForm(forms.ModelForm):
    class Meta:
        model = add_tickets_form
        fields = ['title','description','priority','type']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_form
        fields = ['comment']
        