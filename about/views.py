from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    """
    Renders the About Me page with content from the About model.
    
    **Content**
    
    ``about_me``
        an instance of model : `about.about`
        
    **Template**
    
    :template:`about/about_me.html`
    """
    about_content = About.objects.all().order_by('-updated_on').first()
    return render(request, 'about/about_me.html', {'about': about_content})