from django import forms
from .models import Category, SubCategory, News
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'category', 'image' , 'short_description', 'description', 'status')
        exclude = ('id',)

        labels = {
            'title':'शीर्षक', 
            'category':'श्रेणी', 
            'image':'चित्र' , 
            'short_description':'छोटो वर्णन', 
            'description':'वर्णन', 
            'status':'स्थिति', 
            # 'sponsor':'प्रायोजक', 
            # 'world_wide':'विश्व व्यापी'
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'शीर्षक....'}), 
            'category':forms.Select(attrs={'class':'form-control'}), 
            'image':forms.FileInput(attrs={'class':'form-control'}) , 
            'short_description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'छोटो वर्णन....'}),
            'description':CKEditorUploadingWidget(), 
            'status':forms.Select(attrs={'class':'form-control'}), 
          
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug', 'image')
        exclude = ('id',)

        labels ={
            'name':'नाम',
            'slug': 'अंग्रेजी मा नाम',
            'image':'श्रेणी को छवि'
        }

        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'नाम...'}),
            'slug':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'अंग्रेजी मा नाम'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'accept':'image/*'})
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('name','slug','category', 'image')
        exclude = ('id',)

        labels ={
            'name':'उप श्रेणी नाम',
            'category':'श्रेणी',
            'slug': 'अंग्रेजी मा नाम',
            'image':'उप श्रेणी को छवि'
        }

        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'नाम...'}),
            'category':forms.Select(attrs = {'class':'form-control'}),
            'slug':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'अंग्रेजी मा नाम'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'accept':'image/*'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation


class PasswordChangeFormUpdate(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'placeholder':'Enter New Password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'placeholder':'Enter New Password Again'}),
    )
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True , 'class':'form-control', 'placeholder':'Enter Your Old Password'}
        ),
    )