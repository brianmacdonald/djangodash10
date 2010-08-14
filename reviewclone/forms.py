from django import forms

from reviewclone.models import Review, Relation

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
 
