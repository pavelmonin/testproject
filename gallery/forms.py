from django import forms 
from .models import *

class PictForm(forms.ModelForm): 
  
    class Meta: 
        model = Pict 
        fields = [ 'picture','comment'] 
        
        widgets = {
            'comment': forms.Textarea (attrs={'cols': 40, 'rows': 10}),
        }

        labels = {
            'picture':('Изображение'),
            'comment': ('Комментарий'),           
        }