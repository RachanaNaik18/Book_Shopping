from django import forms
from django.utils.safestring import mark_safe
from .models import book

class HorizontalRadioRenderer(forms.RadioSelect):
     def render(self):
          return mark_safe(u'\n'.join([u'%s\n' %w for w in self]))
     
class book_form(forms.ModelForm):
     
     cat = (('Novel', 'Novel'), ('Journal', 'Journal'), ('Comics', 'Comics'))
     category = forms.ChoiceField(choices=cat,
                                  initial=0,
                                    widget=forms.RadioSelect)

     Lan = (('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'))
     Language = forms.ChoiceField(choices=Lan,
                                  initial=0,
                                    widget=forms.RadioSelect)

     gen = (('Adventure', 'Adventure'), ('Romance', 'Romance'), ('Comedy','Comedy'), ('Action', 'Action'), ('Horror', 'Horror'), ('Psycology', 'Psycology'), ('Spiritual','Spiritual'),('Mythological Friction', 'Mythological Friction'))
     Genra = forms.ChoiceField(choices=gen, widget=forms.Select)

     class Meta:
          model = book
          fields = '__all__'