from django import forms



  
#The choices to choose from
DEPARTMENTS =(
    ( "BCH","biochemistry"),
    ( "EE","electrical engineering"),
    ( "BTC", "biotechnology"),
    ("MCB","microbiology"),
    ( "BIO","biology"),
    ( "CE", "chemical engineering"),
    ( "OPT", "Optometry"),
    ( "SE", "software engineering"),
    ( "PUT", "public Health"),
    ("STA", "statistics" ),
    
)
  
# creating a form 
class ChoiceForm(forms.Form):
    departments  = forms.ChoiceField(choices = DEPARTMENTS)