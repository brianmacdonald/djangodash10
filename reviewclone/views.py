
from django.shortcuts import render_to_response

from reviewclone.models import Item, Review, Relation, Simular
from utils import find_simular

@login_required
def create_relation(request, template_name="reviewclone/new_relation.html"):
    if request.POST:
        user_2_id = request.POST.get('user')
        user_2 = get_object_or_404(User, pk=user_2_id)
        # This *could* be a get method...
        user_relation = Relation.objects.filter(
            user_1 = request.user,
            user_2 = user_2, 
        )
        form = RelationForm(request.POST)
        if form.is_valid() and user_relation.count() < 1:
            form.instance.user_1 = request.user
            form.save()
    else:
        form = RelationForm()
    return render_to_response()

@login_required
def delete_relation(request, template_name="reviewclone/delete_relation.html"):
    if request.POST:
        user_2_id = request.POST.get('user')
        user_2 = get_object_or_404(User, pk=user_2_id)
        form = RelationForm(request.POST)
        # TODO: Finish this
    else:
        form = RelationForm()
    return render_to_response()

@login_required
def relations_list(request, template_name="reviewclone/relations_list.html"):
    user_relations = Relation.objects.filter(user=request.user)
    return render_to_response(
        template_name,
        {
            'object_list': user_relations,
        },
        context_instance=RequestContext(request)
    )     

@login_required
def dashboard(request, template_name="reviewclone/dashboard.html"):
    """Combination list of users reviews and followies reviews"""
    relation_users = Relation.objects.filter(user_1=request.user)
    user_reviews = Reviews.object.filter(
        Q(user=response.user|user__in=relation_users.values_list('user_2'))
    )
    return render_to_response(
        template_name,
        {
            'object_list': reviews,
        },
        context_instance=RequestContext(request)
    )

@login_required
def user_reviews(request, username, template_name="reviewclone/user_review_list.html"):
    user = get_object_or_404(User, username=username)
    reviews = Reviews.object.filter(user=user)
    return render_to_response(
        template_name,
        {
            'object_list': reviews,
        },
        context_instance=RequestContext(request)
    )

@login_required
def simular_list(request, template_name="reviewclone/simular_list.html"):
    simular_dict = find_simular(request.user)
    # Remove old
    Simular.objects.filter(user_1=request.user).delete()
    for user, count in simular_dict.iteritems():
        Simular(
            user_1=request.user,
            user_2=user,
            count=count
        ).save() 
    simular = Simular.objects.filter(user_1=request.user)
    return render_to_response(
        template_name,
        {
            'object_list': simular,
        },
        context_instance=RequestContext(request)
    )

def items_list(request, first_letter=None, template_name="reviewclone/items_list.html"):
    if first_letter:
        items = Item.objects.filter(name__startswith=letter)
    else:
        items = Item.objects.all()
    return render_to_response(
        template_name,
        {
            'object_list': simular,
        },
        context_instance=RequestContext(request)
    )

@login_required
def create_review(request, item_id, template_name="reviewclone/create_review.html"):
    review_exist = False
    if request.POST:
        item = get_object_or_404(Item, pk=item_id)
        form = ItemForm(request.POST)
        if Unit.object.filter(item=item, user=request.user):
             review_exist = True
        if form.is_valid() and not review_exist:
            form.instance.user_1 = request.user
            form.save()
    else:
        form = ItemForm()
    return render_to_response(
        template_name,
        {
            'form': form,
        },
        context_instance=RequestContext(request)
    )
 
@login_required
def after_review(request, review_id):
    # check review count
    
    # if review count is not greater than n
        # Force to next review

    # 
    pass
 
