from django.shortcuts import render
from .form import FeaturesForm
import requests
import json

# Create your views here.
def home_view(request):
    
    form = FeaturesForm(request.POST or None) #je reprends le formulaire (les inputs)
    if request.method == 'POST': 
        form = FeaturesForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            reponse = requests.post('http://127.0.0.1:8001/predict', data=data)
            info = reponse.text # réponse de la requête qu'on a mis en format text 
            return render(request, 'home_page.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'home_page.html', context=context )