from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.template import loader #old, not used
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .models import Bet, Choice, MyBets


def index(request):
    latest_bet_list = Bet.objects.order_by('-pub_date')[:5]
    context = {'latest_bet_list': latest_bet_list}
    return render(request, 'bet_app/index.html', context)

def mybets(request):
    print('it is running')
    the_thing = MyBets.objects.filter(user_id=request.user.id)
    # the_thing2 = the_thing.bet_taken.bet_text
    return render(request, "bet_app/mybets.html", {'the_thing': the_thing})

def detail(request, bet_id):
    bet = get_object_or_404(Bet, pk=bet_id)
    return render(request, "bet_app/detail.html", {'bet': bet})

def results(request, bet_id):
    bet = get_object_or_404(Bet, pk=bet_id)
    return render(request, 'bet_app/results.html', {'bet': bet})


def vote(request, bet_id):
    bet = get_object_or_404(Bet, pk=bet_id)
    #get_bet = MyBets.objects.all().filter(bet_taken=bet_id)
    #my_bets_list = get_object_or_404(MyBets, user_id=request.user.id)
    add_my_bet = MyBets()
    try:
        selected_choice = bet.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'bet_app/detail.html', {'bet': bet, 'error_message': "You didn't select a choice."})
    else:
        for b in bet.choice_set.all():
            b.is_chosen = False
            b.save()
        selected_choice.is_chosen = True
        selected_choice.save()

        if MyBets.objects.filter(bet_taken=bet_id, user_id=request.user.id).exists():
            pass
        else:
            # add_my_bet.user = request.user
            # add_my_bet.bet_taken = bet_id
            # add_my_bet.save()

            MyBets.objects.create(
            user = request.user,
            bet_taken = Bet.objects.get(pk=bet_id))

        return HttpResponseRedirect(reverse('bet_app:results', args=(bet.id,)))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # return redirect('/account/profile/{}/'.format(user.id))
            return redirect('/bullsbet/')
    else:
        form = UserCreationForm()
    return render(request, 'bet_app/register.html', context={'form': form})
