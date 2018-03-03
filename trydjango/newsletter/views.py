# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from forms import SignUpForm, ContactForm, SlidersForm
import urlparse
from django.http import HttpResponse
from subprocess import call
import os
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate ,  login, logout
from django.contrib.auth.decorators import login_required
from django import forms



# Create your views here.
def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/sliders') 
	title = "Welcome! Login please to be able to reconfigure the robot parameters"
	invalid = False
	# if request.user.is_authenticated():
	# 	title = "My title is %s" %(request.user)

	form = SignUpForm(request.POST or None)
	
	if form.is_valid():
		username= form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username,password=password)
	
	  #instance =	form.save(commit=True)
	  	if user is not None:
	  		if user.is_active:
	  			login(request,user)
	  			return HttpResponseRedirect("/sliders/")
	  	else:
	  		invalid = True

	#  if not instance.full_name :
	#  	instance.full_name = "Justin"
	#  instance.save()

		#instance.save()
	# 	#print instance
	context = {
	"title": title,
	"form": form,
	"invalid": invalid

	 }
	
	return render(request,"home.html",context)

# def form(request):
# 	print(request.body)
# 	body = request.body
# 	if body:
# 		parsed = body.split("&")
# 		my1 = parsed[1].split('=')[1]
# 		my2 = parsed[2].split('=')[1]
# 		my3 = parsed[3].split('=')[1]
# 		my4 = parsed[4].split('=')[1]
# 		print my1 , my2, my3, my4
# 		return HttpResponse("wE RECEIVED THE DATA FROM POST REQ"+my1 + my2 + my3 + my4)

	form = ContactForm2(request.POST or None)
	print("We are here")
	# if form.is_valid():
	#  instance =	form.save(commit=True)
	#  if not instance.full_name :
	#  	instance.full_name = "Justin"
	#  instance.save()

	# 	instance.save()
	# 	#print instance
	# context = {
	# "title": title,
	# "form": form
	# } 
	# print(request.POST)
	# print(form.myRange1)
	return render(request,"sliders.html",{})

def contact(request):
	form = ContactForm(request.POST or None)
	# if form.is_valid(): ## we can't save it
	# 	for key in form.cleaned_data:
	# 		print key
	# 		#print form.cleaned_data.get(key)
		#print form.cleaned_data
	#email = form.cleaned_data("email")
	# message = form.cleaned_data("message")
	# full_name = form.cleaned_data("full_name")
	if form.is_valid():
		print form.cleaned_data
	context = {

			"form": form,
	}
	return render(request,"home.html",context)




def sliderPage(request):
 if not request.user.is_authenticated():
	return HttpResponseRedirect('/') 
 MyForm = SlidersForm(request.POST or None)
 if MyForm.is_valid():
		max_velocity_       = MyForm.cleaned_data.get("max_velocity")
		max_turn_rate_      = MyForm.cleaned_data.get("max_turn_rate")
		line_row_location_  = MyForm.cleaned_data.get("line_row_location")
		LF_K_p_ 			= MyForm.cleaned_data.get("LF_K_p")
		LF_K_i_ 			= MyForm.cleaned_data.get("LF_K_i")
		LF_K_d_ 			= MyForm.cleaned_data.get("LF_K_d")
		LF_windup_limit_    = MyForm.cleaned_data.get("LF_windup_limit")
		target_distance_    = MyForm.cleaned_data.get("target_distance")
		BD_K_p_  			= MyForm.cleaned_data.get("BD_K_p")
		BD_K_i_ 			= MyForm.cleaned_data.get("BD_K_i")
		BD_K_d_ 			= MyForm.cleaned_data.get("BD_K_d")
		BD_windup_limit_    = MyForm.cleaned_data.get("BD_windup_limit")
		#print max_velocity_, max_turn_rate_,line_row_location_, LF_K_p_, LF_K_i_, LF_K_d_, LF_windup_limit_, target_distance_ , BD_K_p_, BD_K_i_, BD_K_d_, BD_windup_limit_
		Parameters = ("max_velocity: "+ max_velocity_ + "\n" 
		+  "max_turn_rate: " + max_turn_rate_ + "\n" 
		+ "line_row_location: " + line_row_location_ +"\n" 
		+  "LF_K_p: " + LF_K_p_ +"\n"
		+ "LF_K_i: " + LF_K_i_  + "\n" 
		+ "LF_K_d: " + LF_K_d_  + "\n" 
		+  "LF_windup_limit: "+ LF_windup_limit_  +"\n" 
		+ "target_distance: "+ target_distance_  + "\n" 
		+  "BD_K_p: "+ BD_K_p_  +"\n" 
		+  "BD_K_i: "+ BD_K_i_  + "\n" 
		+  "BD_K_d: "+ BD_K_d_ + "\n" 
		+  "BD_windup_limit: "+ BD_windup_limit_)
		yaml = open("parm.yaml","w")
		yaml.write(Parameters)
		yaml.close()
		# cwd= os.getcwd()
		# print cwd
		call(["rosrun","dynamic_reconfigure","dynparam","load","/reflekte","parm.yaml"])


 return render(request,"forms.html",{})
