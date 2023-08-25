from django import forms
from app1.models import emp,News,holiday

class empForm(forms.ModelForm):
	class Meta:
		model = emp
		fields = "__all__"

class newsForm(forms.ModelForm):
	 class Meta:
	 	model = News
	 	fields = "__all__"

class holidayForm(forms.ModelForm):
	 class Meta:
	 	model = holiday
	 	fields = "__all__"