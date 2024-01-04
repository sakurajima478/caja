from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistroUsuario, LoginUsuario

def inicio(request):
    return render(request, "pages/core/inicio.html")

def signIn(request):
    if request.method == 'GET':
        return render(request, 'pages/core/login.html', context={
            'form' : LoginUsuario,
        })
    
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if usuario is None:
            messages.warning(request, 'El usuario o la cotraseña no son validos!')
            return render(request, 'pages/core/login.html', context={
                    'form' : LoginUsuario,
                })
        else:
            login(request, usuario)
            return redirect('caja:caja')

def registro(request):
    if request.method == 'GET':
        return render(request, 'pages/core/registro.html', context={
            'form' : RegistroUsuario,
        })
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                messages.success(request, 'Usuario registrado correctamente!')
                return redirect('caja:caja')
            
            except IntegrityError:
                messages.warning(request, 'El usuario ya existe!')
                return render(request, 'pages/core/registro.html', context={
                    'form' : RegistroUsuario,
                })
          
        messages.warning(request, 'Las Contraseñas no coinciden!')      
        return render(request, 'pages/core/registro.html', context={
            'form' : RegistroUsuario,
        })

def salir(request):
    logout(request)
    return redirect('inicio')