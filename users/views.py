from django.contrib import auth
from django.shortcuts import render, redirect
from users.extra.google import Google
from users.models import User


def login(request):
    print(request.user.is_authenticated)
    return render(request, 'users/in.html')


def callback(request):
    g_auth = Google.auth(request.GET['code'])
    if g_auth['status'] == 200:
        g_info = Google.info(auth=g_auth)
        search = User.objects.filter(uid=g_info['id'])
        if bool(search):
            user = search[0]
        else:
            g_info['uid'] = g_info.pop('id')
            user = User(**g_info)
            user.save()
        auth.login(request, user)
    return redirect('in')


def out(request):
    auth.logout(request)
    return redirect('in')
