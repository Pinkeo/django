from django import forms 
from .models import Post, Category

#category = [('coding','coding'),('uncategorized','uncategorized'),('Advice','Advice'),('Life','Life')]

category = Category.objects.all().values_list('name','name')
category_list = []
for item in category:
	category_list.append(item)




class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','category','body','snippet')

		widgets = {
				'title': forms.TextInput(attrs={'class':'form-control'}),
				'title_tag':forms.TextInput(attrs={'class':'form-control'}),
				'author': forms.Select(attrs={'class':'form-control'}),
				'category': forms.Select(choices=category_list, attrs={'class':'form-control'}),
				'body': forms.Textarea(attrs={'class':'form-control'}),
				'snippet': forms.Textarea(attrs={'class':'form-control'}),


		}
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','body','category','snippet')

		widgets = {
				'title': forms.TextInput(attrs={'class':'form-control'}),
				'title_tag':forms.TextInput(attrs={'class':'form-control'}),
				'category': forms.Select(choices=category_list, attrs={'class':'form-control'}),

				#'author': forms.Select(attrs={'class':'form-control'}),
				'body': forms.Textarea(attrs={'class':'form-control'}),
				'snippet': forms.Textarea(attrs={'class':'form-control'}),

		}