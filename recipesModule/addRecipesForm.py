from django import forms

class AddRecipe(forms.Form):
	name = forms.CharField(max_length=200)
	category =  forms.CharField(max_length=100)
	country =  forms.CharField(max_length=100)