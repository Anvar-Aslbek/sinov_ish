from django.shortcuts import redirect, render

from .forms import BahoForm
from .models import Talaba, Fan, Baho

def home(request):
    user1 = Talaba.objects.get(username="Yusufbek") #request.user ga almashtiramiz
    fanlar = Fan.objects.filter(fakultet=user1.fakultet)
    print(user1.fakultet.name)
    print("Salom")
    if request.method == 'POST':
        print("Salom11")
        a = request.POST.items()
        d = 0
        for keys,values in a:
            if d==0:
                d=1
                continue
            fan1 = Fan.objects.get(id=keys)
            k = Baho.objects.filter(user=user1,fan=fan1).exists()
            if k:
                lk = Baho.objects.get(user=user1,fan=fan1)
                lk.baho = values
                lk.save()
            else:
                f = Baho()
                f.user = user1
                f.fan = fan1
                f.baho = values
                f.save()
            print("Ciqdi",keys, values, type(keys), type(values))
        return redirect('register')
    else:
        form = BahoForm()
    return render(request,'index.html', {'form':form, 'fanlar':fanlar})

def jadval(request):
    return render(request,"jadval.html")