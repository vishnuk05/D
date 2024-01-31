from .models import signup
from django import forms



class addform(forms.ModelForm):

    gender = forms.ChoiceField(choices=signup.GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:

        model = signup

        fields = ("firstname",'lastname','email','phone','image','gender','username','password','confirm_password')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }