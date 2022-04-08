from django.shortcuts import redirect, render

from Sinov_ish.models import baho
from .forms import BahoForm
from .models import Talaba, Fan

def home(request):
    user1 = Talaba.objects.get(username="Yusufbek") #request.user ga almashtiramiz
    fanlar = Fan.objects.filter(fakultet=user1.fakultet)
    print(user1.fakultet.name)
    print("Salom")
    if request.method == 'POST':
        print("Salom11")
        form = BahoForm(request.POST)
        if form.is_valid():
            print("Salom1")
            f = form.save(commit=False)
            f.user = user1
            f.save()
            return redirect('home')
    else:
        form = BahoForm()
    return render(request,'index.html', {'form':form, 'fanlar':fanlar})
