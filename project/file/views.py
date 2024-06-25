from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileForm
from .models import File
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def index(request):
    form = FileForm()
    context = {}
    context['form'] = form
    files = File.objects.all()
    niveaux = ["CE1","CE2", "CM1", "CM2", "6eme", "5eme", "4eme", "3eme"]
    context['niveaux'] = niveaux
    context['files'] = files
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('index')
    return render(request, 'index.html', context)
    

def home(request):
    form = FileForm()
    context = {}
    context['form'] = form
    files = File.objects.all()
    niveaux = ["CE1","CE2", "CM1", "CM2", "6eme", "5eme", "4eme", "3eme"]
    context['niveaux'] = niveaux
    context['files'] = files
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('home')
    return render(request, 'home.html', context)

def uploadfichier(request):
    form = FileForm()
    context = {}
    context['form'] = form
    files = File.objects.all()
    niveaux = ["CE1","CE2", "CM1", "CM2", "6eme", "5eme", "4eme", "3eme"]
    context['niveaux'] = niveaux
    context['files'] = files
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('upload')
    else:
        context['form'] = form 
    
    return render(request, 'upload.html', context)


def niveau(request, niveau):
    context = {}
    if niveau in ["CE2", "CM1", "CM2"]:
        matieres = ["Maths", "Français", "Anglais", "Histoire-Geo", "Sciences"]
    else:
        matieres = ["Maths", "Français", "Anglais", "Histoire-Geo", "Physique-Chimie", "SVT"] 
    context['matieres'] = matieres
    context['niveau'] = niveau
    return render(request, 'matieres.html',context)


def matiere(request, niveau, matiere): 
    context = {}
    files = File.objects.all()
    niveaux = ["CE1","CE2", "CM1", "CM2", "6eme", "5eme", "4eme", "3eme"]
    files = files.filter(niveau=niveau,matiere=matiere)
    context['files'] = files
    context['niveau'] = niveau
    context['matiere'] = matiere
    
    if request.method == 'POST':
        if 'file_id' in request.POST:
            file_id = request.POST.get('file_id')
            file_obj = File.objects.get(id=file_id)
            response = HttpResponse(file_obj.file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{file_obj.caption}.pdf"'
            return response
        if 'delete' in request.POST:
            file_id = request.POST.get('delete')
            file = File.objects.get(id=file_id)
            file.delete()
            return redirect('matiere', niveau, matiere)
        
    return render(request, 'matiere.html',context)


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
           return HttpResponse("les mots de passes de sont pas pareils")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return HttpResponse("compte créé")
    return render(request,'signup.html')
 

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Erreur de connexion")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


    



