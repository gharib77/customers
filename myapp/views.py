from myaccounts.models import Myuser
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MvtForm

from myapp.models import Personne
from myapp.filters import FpersFilter,PersonneFilter
from myapp.forms import FormPers
from datetime import datetime,date
#from . import filters
#pagination
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
#from django.conf import settings
#from myaccounts.models import Myuser
@login_required
def index(request):
    a=10
    b=5
    age=78
    nom="driss"
    print(f"la multiplicatio de {a} par {b} est: {a*b}")
    print("mon ami {} a {} ans".format(request.user.prenom,age))
    wdate1= date.today().strftime("%d/%m/%Y")
    wdate2= datetime.now()
    all_var={'nom':"azzouz",'prenom':'jouali','age':25}
    form=MvtForm( all_var,user=request.user)
    #print(request.user.prenom)
    return render(request,'myapp/index.html',{'form':form,'wdate1':wdate1,'wdate2':wdate2})
def index1(request):
    personnes=Personne.objects.all()
    filter = FpersFilter(request.GET, queryset=personnes)
    return render(request,'myapp/index1.html',{'filter':filter})

def list1(request):
    personnes=Personne.objects.all()
    paginator=Paginator(personnes,3)    #2 per page
    page=request.GET.get('page')        #Page requested in the previous paragraph,For example, click'next page',This page takes variables as'page'express
    try:
      personne_obj=paginator.page(page) #Gets the number of pages requested by the front end
    except PageNotAnInteger:
        personne_obj=paginator.page(1)   #If the front-end input is not a number,Just go back to page one
    except EmptyPage:
        personne_obj=paginator.page(paginator.num_pages)
    return render(request,'myapp/list1.html',{'personnes':personne_obj})

def addpers(request):
    form=FormPers(request.POST or None,user=request.user)
    if form.is_valid():
        #return HttpResponse(form)
        wdate=form.cleaned_data['date_entr']
        print(f"yeardate {wdate.year} monthdate {wdate.month} daydate {wdate.day}")
        print(f"date : {type(form.cleaned_data['date_entr'])} {form.cleaned_data['date_entr']}")
        form.save()
        return redirect('myapp:list1')
    return render(request,'myapp/addpers.html',{'form':form})

def editpers(request,pk):
    personne=get_object_or_404(Personne,pk=pk)
    form=FormPers(request.POST or None, instance=personne)
    if form.is_valid():
        wdate= form.cleaned_data['date_entr']
        instance= form.save(commit=False)
        instance.year_prod=wdate.year
        instance.save()
        return redirect('myapp:list1')
    return render(request,'myapp/editpers.html',{'form':form})

def listpage(request):
    wdate=datetime.now()
    wdate1=date.today()
    print(wdate1)
    personnes= Personne.objects.all()
    #filter data
    myfilter = PersonneFilter(request.GET,queryset=personnes)
    personnes=myfilter.qs
    paginator=Paginator(personnes,3)
    page=request.GET.get('page')
    #pers=paginator.get_page(page)
    
    try:
        pers=paginator.page(page)
    except PageNotAnInteger:
        pers=paginator.page(1)
    except EmptyPage:
        pers=paginator.page(paginator.num_pages)
       
    context={'personnes':personnes,'wdate':wdate,'pers':pers,'myfilter':myfilter}
    return render(request,'myapp/listpage.html',context)
def listpage1(request):
    context = {
        'pers': Personne.objects.order_by('id').all()
    }
    return render(request, 'myapp/listpage1.html', context)


