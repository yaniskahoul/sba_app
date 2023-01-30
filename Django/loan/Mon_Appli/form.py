from django import forms

# création du formulaire

class FeaturesForm(forms.Form):
    State = forms.CharField(max_length= 100, initial= 'NV')
    NAICS =  forms.IntegerField(initial=23)
    Term = forms.IntegerField(initial=1)
    FranchiseCode = forms.IntegerField(initial=1)
    UrbanRural = forms.IntegerField(initial=1)
    GrAppv = forms.IntegerField(initial=250000)

