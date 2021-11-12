from django.shortcuts import render
from .forms import  ChoiceForm
  
# Create your views here.
def home(request):
    form = ChoiceForm()
    context = {
        'form': form
    }
    return render( request,"app/home.html", context)