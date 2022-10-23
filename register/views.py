from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("homepage")
		messages.error(request, "Error en el registro, revisa la información entregada.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
    

def hola(request):
    return render(request, "mainpage.html")