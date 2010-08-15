from django import forms

from reviewclone.models import Review, Relation

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude=('user', 'item',)

class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        exclude=('user_1', 'type', 'is_active')
 
