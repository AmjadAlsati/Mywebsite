from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	message = forms.CharField()

# class ContactForm2(forms.Form):
# 	print("Here")
# 	myRange1 = forms.CharField(label="myRange1")
# 	print(myRange1)
# 	# myRange2 = forms.myRange2
# 	# myRang3 = forms.myRang3
# 	# myRange4 = forms.myRange4
	
class SignUpForm(forms.ModelForm):
	class Meta:
		model= SignUp
		fields =  '__all__'  #{'full_name','password'}
		exclude = ['email','address']
		widgets = {
        'password': forms.PasswordInput(),
    	}

	def clean_email(self):
		 	
			email = self.cleaned_data.get('email')
			email_base,provider = email.split("@")
			domain, extension = provider.split('.')
			# if not domain == "USC":
			# 	raise forms.ValidationError("Please make sure you use your USC email.")
			if not extension == "edu":				
				raise forms.ValidationError("Pleas use a valid .edu email address")
		
			return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	print full_name
	# 	return full_name


class SlidersForm(forms.Form):
	max_velocity = forms.CharField(label="max_velocity")
	max_turn_rate = forms.CharField(label="max_turn_rate")
	line_row_location = forms.CharField(label="line_row_location")
	LF_K_p = forms.CharField(label="LF_K_p")
	LF_K_i = forms.CharField(label="LF_K_i")
	LF_K_d = forms.CharField(label="LF_K_d")
	LF_windup_limit = forms.CharField(label="LF_K_d")
	target_distance = forms.CharField(label="target_distance")
	BD_K_p = forms.CharField(label="BD_K_p")
	BD_K_i = forms.CharField(label="BD_K_i")
	BD_K_d = forms.CharField(label="BD_K_d")
	BD_windup_limit = forms.CharField(label="BD_windup_limit")






	