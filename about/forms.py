#from .models import Comment
from .models import CollaborateRequest
from django import forms


#class CommentForm(forms.ModelForm):
 #   class Meta:
  #      model = Comment
   #     fields = ('body',)




class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')


