from django import forms


from .models import BlogPost

class NewBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'author', 'status']

