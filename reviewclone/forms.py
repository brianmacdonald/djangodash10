from django import forms

from reviewclone.models import Review, Relation

class ReviewForm(forms.ModelForm):
    post_review_message = forms.BooleanField(
        label="Post my review on Facebook",
        initial=True,
        required=False,
    )
    class Meta:
        model = Review
        exclude=('user', 'item',)

class RelationForm(forms.ModelForm):
    post_relation_message = forms.BooleanField(
        label="Post on Facebook",
        initial=True,
        required=False,
    )
    class Meta:
        model = Relation
        exclude=('user_1', 'type', 'is_active')
 
