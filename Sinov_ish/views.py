from django.shortcuts import redirect, render

from .forms import BahoForm
from .models import Talaba, Fan, Baho, Fakultet

def home(request):
    user1 = Talaba.objects.get(username=request.user)
    fanlar = Fan.objects.filter(fakultet=user1.fakultet)
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
        return redirect('jadval')
    else:
        form = BahoForm()
    return render(request,'index.html', {'form':form, 'fanlar':fanlar})

def jadval(request):
    user = request.user
    fanlar = Fan.objects.filter(fakultet=user.fakultet)
    users = Talaba.objects.filter(fakultet=user.fakultet)
    content = {
        'fanlar':fanlar,
        'users':users
    }
    return render(request,"jadval.html", content)
def search(request):
    results = None
    try:
        query = request.POST['query']
        results = Talaba.objects.filter(name__icontains=query)

        return render(
            request,
            'jadval.html',
            {'jadval': results}
        )
    except KeyError:
        "KeyError"
        return render(
            request,
            'jadval.html',
            {'jadval': results}
        )
