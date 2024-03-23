from django.shortcuts import render
from .forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'ufo':UFO, 'pfo':PFO}
    if request.method == 'POST' and request.FILES :
        ufo = UserForm(request.POST)
        pfo = ProfileForm(request.POST, request.FILES)
        if ufo.is_valid() and pfo.is_valid():
            mufo = ufo.save(commit = False)
            pswd = ufo.cleaned_data['password']
            mufo.set_password(pswd)
            mufo.save()

            mpfo = pfo.save(commit = False)
            mpfo.username = mufo
            mpfo.save()
            return HttpResponseRedirect(reverse('userlogin'))
            
        else:
            return HttpResponse('Invalid Data')     
    return render(request, 'register.html',d)



def userlogin(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pswd']
        AUO = authenticate(username=username, password=password)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = username
            return render(request, 'home.html', {'un':username})
        else:
            return HttpResponse('<center>Invalid Credentials</center>')
    return render(request,'login.html')


def home(request):
    un = request.session.get('username')
    if un:
        return render(request,'home.html',{'un':un})
    return render(request, 'home.html')

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userlogin'))

@login_required
def display_profile(request):
    un = request.session.get('username')
    uno = User.objects.get(username = un)
    po = UserProfile.objects.get(username = uno)
    d = {'un': uno, 'po':po}
    return render(request, 'display_profile.html',d)

def resetpswd(request):
    if request.method == 'POST':
        ps1 = request.POST['ps']
        rps = request.POST['rps']
        return HttpResponse('HI')
    return render(request,'resetpswd.html')

def forgotpswd(request):
    if request.method == 'POST':
        un = request.POST['un']
        uo = User.objects.get_or_create(username = un)
        if uo[0]:
            ps = request.POST['ps']
            rps = request.POST['rps']
            if ps == rps :
                uo[0].set_password(ps)
                uo[0].save()
            else:
                return render(request, 'forgotpswdermsg.html',{'ermsg':'Passwords mismatch !!'})
    return render(request, 'forgotpswd.html')

    


