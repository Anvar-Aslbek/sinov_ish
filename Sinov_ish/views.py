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
    baholar = Baho.objects.filter(fan__in=fanlar)
    content = {
        'fanlar':fanlar,
        'jadval':users,
        'baholar':baholar,
    }
    return render(request,"jadval.html", content)


def search(request):
    results = None
    user = request.user  
    fanlar = Fan.objects.filter(fakultet=user.fakultet)
    baholar = Baho.objects.filter(fan__in=fanlar)
    try:
        query = request.POST['query']
        results = Talaba.objects.filter(username__icontains=query, fakultet=user.fakultet)

        return render(
            request,
            'jadval.html',
            {'jadval': results,'fanlar':fanlar,'baholar':baholar}
        )
    except KeyError:
        "KeyError"
        return render(
            request,
            'jadval.html',
            {'jadval': results,'fanlar':fanlar}
        )
        