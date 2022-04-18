from pickle import FALSE
from django.shortcuts import redirect, render
from .forms import BahoForm
from .models import Talaba, Fan, Baho, Fakultet
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

        #####STIPENDIYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        baho2 = Baho.objects.filter(user = user1,baho='2')
        baho3 = Baho.objects.filter(user = user1,baho='3')
        if len(baho2)>=4:
            user1.stipendiya = "yiqilgan"
            user1.save()
        elif len(baho3)>=2:
            user1.stipendiya = "olmaydi"
            user1.save()
        else:
            user1.stipendiya = "oladi"
            user1.save()

        return redirect('jadval')
    else:
        form = BahoForm()
    return render(request,'index.html', {'form':form, 'fanlar':fanlar})

@login_required(login_url='login')
def jadval(request):
    user = request.user
    fanlar = Fan.objects.filter(fakultet=user.fakultet)
    users = Talaba.objects.filter(fakultet=user.fakultet)
    baholar = Baho.objects.filter(fan__in=fanlar)
    #ishlamay qolganda komentariyani olib tashlang
    # USER = Talaba.objects.all()
    # for o in USER:
    #     user1 = o
    #     baho2 = Baho.objects.filter(user = user1,baho='2')
    #     baho3 = Baho.objects.filter(user = user1,baho='3')
    #     fan = Fan.objects.filter(fakultet = user1.fakultet)
    #     us = Baho.objects.filter(user = user1)
    #     if len(us) != len(fan):
    #         user1.stipendiya = "kiritilmagan"
    #         user1.save()
    #     elif len(baho2)>=4:
    #         user1.stipendiya = "yiqilgan"
    #         user1.save()
    #     elif len(baho3)>=2:
    #         user1.stipendiya = "olmaydi"
    #         user1.save()
    #     else:
    #         user1.stipendiya = "oladi"
    #         user1.save()
    
    content = {
        'fanlar':fanlar,
        'jadval':users,
        'baholar':baholar,
        'ls':False
    }
    fan = Fan.objects.filter(fakultet = user.fakultet)
    us = Baho.objects.filter(user = user)
    if len(us) != len(fan):
        user.stipendiya = "kiritilmagan"
        user.save()
        return redirect('home')
    return render(request,"jadval.html", content)

@login_required(login_url='login')
def search_baho(request):
    results = None
    user = request.user
    fanlar = Fan.objects.filter(fakultet=user.fakultet)
    query = request.POST['baho_search']
    baholar3 = Baho.objects.filter(fan__in=fanlar,baho='3')
    baholar2 = Baho.objects.filter(fan__in=fanlar,baho='2')
    ls3 = [True]
    for i in baholar3:
        if not(i.user in ls3):
            ls3.append(i.user)
    for i in baholar2:
        if not(i.user in ls3):
            ls3.append(i.user)
    baholar4 = Baho.objects.filter(fan__in=fanlar,baho='4')
    ls4 = [True]
    for i in baholar4:
        if not(i.user in ls3) and not(i.user in ls4):
            ls4.append(i.user)
    if query == '3':
        ls = ls3
    elif query == '4':
        ls = ls4
    else:
        baholar5 = Baho.objects.filter(fan__in=fanlar,baho='5')
        ls=[True]
        for i in baholar5:
            if not(i.user in ls3) and not(i.user in ls4) and not(i.user in ls):
                ls.append(i.user)
        print(bool(ls))


    baholar = Baho.objects.filter(fan__in=fanlar)
    results = Talaba.objects.filter(fakultet=user.fakultet)

    return render(
        request,
        'jadval.html',
        {'jadval': results,'fanlar':fanlar,'baholar':baholar, 'ls':ls}
    )

@login_required(login_url='login')
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
            {'jadval': results,'fanlar':fanlar, 'ls':False}
        )
        