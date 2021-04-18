from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import EngClassNotes, HinClassNotes, AraClassNotes, MatClassNotes, SciClassNotes, IssClassNotes, UssClassNotes
from .forms import EngClassNotesForm , HinClassNotesForm, AraClassNotesForm , MatClassNotesForm, SciClassNotesForm , IssClassNotesForm, UssClassNotesForm
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('SubPage')
        else:
             messages.info(request, 'user Name or Password is not incorect ')
                   
    return render(request, 'ClassNotes/Home.html')

def SubPage(request):
     return render(request, 'ClassNotes/SubPage.html' )



"""def EngNotes(request):
     return render(request, 'ClassNotes/EngNotes.html')"""

def Upload_Notes(request):
    if request.method == 'POST':
        form = EngClassNotesForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = EngClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Notes.html', {'form':form})

@login_required
def EngNotes(request):
    Notes = EngClassNotes.objects.all()
    return render( request, 'ClassNotes/EngNotes.html', {'Notes': Notes})


"""def HinNotes(request):
     return render(request, 'ClassNotes/HinNotes.html')"""

def Upload_Hin_Notes(request):
    if request.method == 'POST':
        Hin_form = HinClassNotesForm(request.POST , request.FILES)
        if Hin_form.is_valid():
            Hin_form.save()
    else:
        Hin_form = HinClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Hin_Notes.html', {'Hin_form':Hin_form})


def HinNotes(request):
    Hin_Notes = HinClassNotes.objects.all()
    return render( request, 'ClassNotes/HinNotes.html', {'Hin_Notes': Hin_Notes})

def AraNotes(request):
    AraNotes = AraClassNotes.objects.all()
    return render( request, 'ClassNotes/AraNotes.html', {'AraNotes': AraNotes})


def MatNotes(request):
    MatNotes = MatClassNotes.objects.all()
    return render( request, 'ClassNotes/MatNotes.html', {'MatNotes': MatNotes})

def SciNotes(request):
    SciNotes = SciClassNotes.objects.all()
    return render( request, 'ClassNotes/SciNotes.html', {'SciNotes': SciNotes})

def IssNotes(request):
    IssNotes = IssClassNotes.objects.all()
    return render( request, 'ClassNotes/IssNotes.html', {'IssNotes': IssNotes})

def UssNotes(request):
    UssNotes = UssClassNotes.objects.all()
    return render( request, 'ClassNotes/UssNotes.html', {'UssNotes': UssNotes})

def deleteEngNotes(request, pk):
    if request.method =='POST':
        EngNote = EngClassNotes.objects.get(pk=pk)
        EngNote.delete()
    return redirect( 'EngNotes' )    

def deleteHinNotes(request, pk):
    if request.method =='POST':
        HinNote = HinClassNotes.objects.get(pk=pk)
        HinNote.delete()
    return redirect( 'HinNotes' )   

def deleteAraNotes(request, pk):
    if request.method =='POST':
        AraNote = AraClassNotes.objects.get(pk=pk)
        AraNote.delete()
    return redirect( 'AraNotes' )   

def deleteMatNotes(request, pk):
    if request.method =='POST':
        MatNote = MatClassNotes.objects.get(pk=pk)
        MatNote.delete()
    return redirect( 'MatNotes' )   

def deleteSciNotes(request, pk):
    if request.method =='POST':
        SciNote = SciClassNotes.objects.get(pk=pk)
        SciNote.delete()
    return redirect( 'SciNotes' )   

def deleteIssNotes(request, pk):
    if request.method =='POST':
        IssNote = IssClassNotes.objects.get(pk=pk)
        IssNote.delete()
    return redirect( 'IssNotes' )   

def deleteUssNotes(request, pk):
    if request.method =='POST':
        UssNote = UssClassNotes.objects.get(pk=pk)
        UssNote.delete()
    return redirect( 'UssNotes' )   

def Upload_Ara_Notes(request):
    if request.method == 'POST':
        Ara_form = AraClassNotesForm(request.POST , request.FILES)
        if Ara_form.is_valid():
            Ara_form.save()
    else:
        Ara_form = AraClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Ara_Notes.html', {'Ara_form':Ara_form})


def Upload_Mat_Notes(request):
    if request.method == 'POST':
        Mat_form = MatClassNotesForm (request.POST , request.FILES)
        if Mat_form.is_valid():
            Mat_form.save()
    else:
        Mat_form = MatClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Mat_Notes.html', {'Mat_form':Mat_form})


def Upload_Sci_Notes(request):
    if request.method == 'POST':
        Sci_form = SciClassNotesForm (request.POST , request.FILES)
        if Sci_form.is_valid():
            Sci_form.save()
    else:
        Sci_form = SciClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Sci_Notes.html', {'Sci_form':Sci_form})

def Upload_Iss_Notes(request):
    if request.method == 'POST':
        Iss_form = IssClassNotesForm (request.POST , request.FILES)
        if Iss_form.is_valid():
            Iss_form.save()
    else:
        Iss_form = IssClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Iss_Notes.html', {'Iss_form':Iss_form})

def Upload_Uss_Notes(request):
    if request.method == 'POST':
        Uss_form = UssClassNotesForm (request.POST , request.FILES)
        if Uss_form.is_valid():
            Uss_form.save()
    else:
        Uss_form = UssClassNotesForm()
   
    return render( request, 'ClassNotes/Upload_Uss_Notes.html', {'Uss_form':Uss_form})


def logout_Page(request):
    logout(request)
    return redirect('home')
