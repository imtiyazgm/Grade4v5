from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import EngWS , AraWS, HinWS, SciWS, IssWS, UssWS, MatWS
from .forms import EngWSForm, AraWSForm, HinWSForm, UssWSForm, IssWSForm, MatWSForm, SciWSForm
from django.core.files.storage import FileSystemStorage


# Create your views here.

def Upload_Eng_WS(request):
    if request.method == 'POST':
        formWENG = EngWSForm(request.POST , request.FILES)
        if formWENG.is_valid():
            formWENG.save()
            return redirect('EngWsheet')
    else:
        formWENG = EngWSForm()
   
    return render( request, 'worksheets/Upload_Eng_WS.html', {'formWENG':formWENG})
    

def Upload_Ara_WS(request):
    if request.method == 'POST':
        formWARA = AraWSForm(request.POST , request.FILES)
        if formWARA.is_valid():
            formWARA.save()
            return redirect('AraWsheet')
    else:
        formWARA = AraWSForm()
   
    return render( request, 'worksheets/Upload_Ara_WS.html', {'formWARA':formWARA})


def Upload_Hin_WS(request):
    if request.method == 'POST':
        formWHIN = HinWSForm(request.POST , request.FILES)
        if formWHIN.is_valid():
            formWHIN.save()
            return redirect('HinWsheet')
    else:
        formWHIN = HinWSForm()
   
    return render( request, 'worksheets/Upload_Hin_WS.html', {'formWHIN':formWHIN})

def Upload_Mat_WS(request):
    if request.method == 'POST':
        formWMAT = MatWSForm(request.POST , request.FILES)
        if formWMAT.is_valid():
            formWMAT.save()
            return redirect('MatWsheet')
    else:
        formWMAT = MatWSForm()
   
    return render( request, 'worksheets/Upload_Mat_WS.html', {'formWMAT':formWMAT})


def Upload_Sci_WS(request):
    if request.method == 'POST':
        formWSCI = SciWSForm(request.POST , request.FILES)
        if formWSCI.is_valid():
            formWSCI.save()
            return redirect('SciWsheet')
    else:
        formWSCI = SciWSForm()
   
    return render( request, 'worksheets/Upload_Sci_WS.html', {'formWSCI':formWSCI})

def Upload_Iss_WS(request):
    if request.method == 'POST':
        formWISS = IssWSForm(request.POST , request.FILES)
        if formWISS.is_valid():
            formWISS.save()
            return redirect('IssWsheet')
    else:
        formWISS = IssWSForm()
   
    return render( request, 'worksheets/Upload_Iss_WS.html', {'formWISS':formWISS})

def Upload_Uss_WS(request):
    if request.method == 'POST':
        formWUSS = UssWSForm(request.POST , request.FILES)
        if formWUSS.is_valid():
            formWUSS.save()
            return redirect('UssWsheet')
    else:
        formWUSS = UssWSForm()
   
    return render( request, 'worksheets/Upload_Uss_WS.html', {'formWUSS':formWUSS})





def EngWsheet(request):
    Eng_WS = EngWS.objects.all()
    return render( request, 'worksheets/EngWS.html', {'Eng_WS': Eng_WS})    

def AraWsheet(request):
    Ara_WS = AraWS.objects.all()
    return render( request, 'worksheets/AraWS.html', {'Ara_WS': Ara_WS})    


def HinWsheet(request):
    Hin_WS = HinWS.objects.all()
    return render( request, 'worksheets/HinWS.html', {'Hin_WS': Hin_WS})    

def MatWsheet(request):
    Mat_WS = MatWS.objects.all()
    return render( request, 'worksheets/MatWS.html', {'Mat_WS': Mat_WS})    

def SciWsheet(request):
    Sci_WS = SciWS.objects.all()
    return render( request, 'worksheets/SciWS.html', {'Sci_WS': Sci_WS})    

def IssWsheet(request):
    Iss_WS = IssWS.objects.all()
    return render( request, 'worksheets/IssWS.html', {'Iss_WS': Iss_WS})    

def UssWsheet(request):
    Uss_WS = UssWS.objects.all()
    return render( request, 'worksheets/UssWS.html', {'Uss_WS': Uss_WS})    





def deleteEngWS(request, pk):
    if request.method =='POST':
        EngWSD = EngWS.objects.get(pk=pk)
        EngWSD.delete()
    return redirect( 'EngWsheet' )    

def deleteAraWS(request, pk):
    if request.method =='POST':
        AraWSD = AraWS.objects.get(pk=pk)
        AraWSD.delete()
    return redirect( 'AraWsheet' )    


def deleteHinWS(request, pk):
    if request.method =='POST':
        HinWSD = HinWS.objects.get(pk=pk)
        HinWSD.delete()
    return redirect( 'HinWsheet' )    

def deleteMatWS(request, pk):
    if request.method =='POST':
        MatWSD = MatWS.objects.get(pk=pk)
        MatWSD.delete()
    return redirect( 'MatWsheet' )    

def deleteSciWS(request, pk):
    if request.method =='POST':
        SciWSD = SciWS.objects.get(pk=pk)
        SciWSD.delete()
    return redirect( 'SciWsheet' )    

def deleteIssWS(request, pk):
    if request.method =='POST':
        IssWSD = IssWS.objects.get(pk=pk)
        IssWSD.delete()
    return redirect( 'IssWsheet' )    

def deleteUssWS(request, pk):
    if request.method =='POST':
        UssWSD = UssWS.objects.get(pk=pk)
        UssWSD.delete()
    return redirect( 'UssWsheet' )    