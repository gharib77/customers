from django import forms
from .models import Mouvement,Article,Personne,Grade
from crispy_forms.helper import FormHelper

indemnites=[
    ('', '----'),
    (10,'pommes'),
    (20,'tomates'),
    (30,'carottes'),
]
class MvtForm(forms.ModelForm):
    legume=forms.CharField(widget=forms.Select(choices=indemnites))
    nom = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hhhhh'}))
    class Meta:
        model = Mouvement
        fields = '__all__'
    def __init__(self,wname,*args, **kwargs):
        print(wname)
        self.user = kwargs.pop('user',None)
       
        super(MvtForm, self).__init__(*args, **kwargs)  
        #print("ghaa ",self.user)  
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        #self.fields['nom'].label = False
        
        self.fields['article'] = forms.ModelChoiceField(
            queryset=Article.objects.filter(myuser=self.user)
        )
        self.fields['article'].empty_label = None   


def get_my_choices(wpos):
    choices_list=[('','-------------------')]+[(r.id,r.libelle) for r in Grade.objects.filter(position=wpos)]
    return choices_list

class FormPers(forms.ModelForm):
    date_entr = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        )
    class Meta:
        model=Personne
        fields= ['nom','prenom','date_entr','grade']

    def __init__(self,*args, **kwargs):
       
        self.user = kwargs.pop('user',None)
        print(self.user)
        super(FormPers, self).__init__(*args, **kwargs)
        wpos=10  
        #self.fields['grade'] = forms.ChoiceField(
        #   choices=get_my_choices(wpos) )
        print(kwargs)
        self.fields["grade"].choices=get_my_choices(wpos)
        #self.fields["grade"].queryset=Grade.objects.filter(position=20)