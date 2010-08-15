from django.conf import settings 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response, get_object_or_404

from reviewclone.forms import ReviewForm, RelationForm
from reviewclone.models import Item, Review, Relation, Similar
from reviewclone.utils import find_similar

@login_required
def create_relation(request, 
                    template_name="reviewclone/create_relation.html"):
    has_relation = False
    user_2 = None
    if request.POST:
        user_2_id = request.POST.get('user_2')
        user_2 = get_object_or_404(User, pk=user_2_id)
        user_relation = Relation.objects.filter(
            user_1 = request.user,
            user_2 = user_2, 
        )
        if user_relation.count() > 0:
            has_relation = True
        form = RelationForm(request.POST)
        if form.is_valid() and user_relation.count() == 0:
            form.instance.user_1 = request.user
            form.save()
            messages.add_message(request, messages.INFO, 
                                'You are now following %s' % user_2)
            return HttpResponseRedirect(reverse('dashboard'))  
    else:
        form = RelationForm()
    return render_to_response(
        template_name,
        {
            'form': form,
            'user_2': user_2,
            'has_relation': has_relation,
        },
        context_instance=RequestContext(request)
    )

@login_required
def delete_relation(request, 
                    template_name="reviewclone/delete_relation.html"):
    user_2 = None
    if request.POST:
        user_2_id = request.POST.get('user_2')
        user_2 = get_object_or_404(User, pk=user_2_id)
        form = RelationForm(request.POST)
        if form.is_valid():
            Relation.objects.filter(
                user_1 = request.user,
                user_2 = user_2,             
            ).delete()
            messages.add_message(request, messages.INFO, 
                                 'You are no longer following %s' % user_2)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = RelationForm()
    return render_to_response(
        template_name,
        {
            'user_2': user_2,
            'form': form,
        },
        context_instance=RequestContext(request)
    )

@login_required
def relations_list(request, 
                   template_name="reviewclone/relations_list.html"):
    user_relations = Relation.objects.filter(user_1=request.user)
    return render_to_response(
        template_name,
        {
            'object_list': user_relations,
        },
        context_instance=RequestContext(request)
    )     

@login_required
def dashboard(request, 
              template_name="reviewclone/dashboard.html"):
    """Combination list of users reviews and followies reviews"""
    relation_users = Relation.objects.filter(user_1=request.user)
    user_reviews = Review.objects.filter(
        Q(user=request.user)|Q(user__in=relation_users.values_list('user_2'))
    ).order_by('-created_at')
    return render_to_response(
        template_name,
        {
            'object_list': user_reviews,
        },
        context_instance=RequestContext(request)
    )

def user_reviews(request, username_slug, 
                 template_name="reviewclone/user_reviews.html"):
    user = get_object_or_404(User, username=username_slug)
    reviews = Review.objects.filter(user=user).order_by('-created_at')
    return render_to_response(
        template_name,
        {
            'user_object': user,
            'object_list': reviews,
        },
        context_instance=RequestContext(request)
    )

@login_required
def similar_list(request, 
                 template_name="reviewclone/similar_list.html"):
    similar_dict = find_similar(request.user)
    # Remove old
    Similar.objects.filter(user_1=request.user).delete()
    for user, count in similar_dict.iteritems():
        Similar(
            user_1=request.user,
            user_2=user,
            count=count
        ).save() 
    similar = Similar.objects.filter(user_1=request.user)
    return render_to_response(
        template_name,
        {
            'object_list': similar,
        },
        context_instance=RequestContext(request)
    )

def items_list(request, letter=None, 
               template_name="reviewclone/items_list.html"):
    if letter:
        items = Item.objects.filter(name__startswith=letter)
    else:
        items = Item.objects.all().order_by('-released')
    return render_to_response(
        template_name,
        {
            'object_list': items,
            'letter': letter,
        },
        context_instance=RequestContext(request)
    )

@login_required
def create_review(request, item_id, 
                  template_name="reviewclone/create_review.html"):
    review_exist = False
    random_item = None
    item = get_object_or_404(Item, pk=item_id)
    if Review.objects.filter(item=item, user=request.user).count() > 0:
        review_exist = True
    if request.POST:
        form = ReviewForm(request.POST)

        if form.is_valid() and review_exist == False:
            form.instance.user = request.user
            form.instance.item = item
            form.save()
            messages.add_message(request, messages.INFO, 
                                'You reviewed %s.' % item)
            return HttpResponseRedirect(reverse('after_review', 
                                                args=[form.instance.pk])) 
    else:
        user_reviews = Review.objects.filter(user=request.user)
        if user_reviews.count() < settings.REVIEWCLONE_REVIEW_MIN:
            random_item = Item.objects.all().exclude(
                pk__in=user_reviews.values_list('item__pk')
            ).order_by('?')[0]
        form = ReviewForm()
    return render_to_response(
        template_name,
        {
            'item': item,
            'review_exist': review_exist,
            'form': form,
            'random': random_item,
        },
        context_instance=RequestContext(request)
    )
 
@login_required
def after_review(request, review_id, 
                 template_name="reviewclone/after_review.html"):
    random_item = None
    review = get_object_or_404(Review, pk=review_id)
    user_reviews = Review.objects.filter(user=request.user)
    # check review count
    if user_reviews.count() < settings.REVIEWCLONE_REVIEW_MIN:
        random_item = Item.objects.all().exclude(
            pk__in=user_reviews.values_list('item__pk')
        ).order_by('?')[0]

    return render_to_response(
        template_name,
        {
            'review': review,
            'user_reviews': user_reviews,
            'random': random_item,
        },
        context_instance=RequestContext(request)
    )        

