from django import forms
from .models import Category, SubCategory, News
from ckeditor_uploader.widgets import CKEditorUploadingWidget
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