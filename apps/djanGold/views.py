from django.shortcuts import render, redirect
import random
import time

def addActivity(request, num, action, location):
    timestamp = time.strftime("(%Y/%m/%d %I:%M %p)")
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d golds from the casino! %s' % (num, timestamp)
            request.session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d golds... Ouch. %s' % (num, timestamp)
            request.session['activity'].append(['lost', lost])
        else:
            print "error"
    elif location == 'farm':
        request.session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        request.session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        request.session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])
    print request.session['activity']


def index(request):
    if 'ninjagold' not in request.session:
        request.session['ninjagold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'djanGold/index.html')

def process(request):
    # print request.POST
    # print "*"*100
    if request.POST['building'] == 'farm':
        request.session['farmgold'] = random.randint(10, 20)
        request.session['ninjagold'] += request.session['farmgold']
        addActivity(request, request.session['farmgold'], 'earned', 'farm')
    elif request.POST['building'] == 'cave':
        request.session['cavegold'] = random.randint(5, 10)
        request.session['ninjagold'] += request.session['cavegold']
        addActivity(request, request.session['cavegold'], 'earned', 'cave')
    elif request.POST['building'] == 'house':
        request.session['housegold'] = random.randint(2, 5)
        request.session['ninjagold'] += request.session['housegold']
        addActivity(request, request.session['housegold'], 'earned', 'house')
    elif request.POST['building'] == 'casino':
        win_lose = random.randint(0, 1)
        if win_lose == 1:
            request.session['casinogold'] = random.randint(0, 51)
            addActivity(request, request.session['casinogold'], 'earned', 'casino')
            request.session['ninjagold'] += request.session['casinogold']
        else:
            request.session['casinogold'] = random.randint(0, 51)
            addActivity(request, request.session['casinogold'], 'lost', 'casino')
            request.session['ninjagold'] -= request.session['casinogold']
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
