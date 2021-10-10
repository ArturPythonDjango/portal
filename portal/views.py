from django.http import HttpResponse
from django.shortcuts import redirect, render
import json


def main(request):
    if 'Registration' in request.POST:
        return redirect("registration/")
    elif 'Authentication' in request.POST:
        return redirect("authentication/")
    return render(request, 'main.html')


def registration(request):
    if 'Registration' in request.POST:
        login = request.POST['log']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        print(login)
        if password2 == password1 and login and password2:
            # READ
            with open("portal/log_sign.json", "r") as my_file:
                signer_json = my_file.read()

            signer = json.loads(signer_json)

            # WRITE
            signer['REGISTER']['LOGIN_INFO']["user_" + login] = {login: password1}
            signer_json = json.dumps(signer)

            with open("portal/log_sign.json", "w") as my_file:
                my_file.write(signer_json)
            return render(request, 'main.html')

        else:
            return HttpResponse("Щось пішло не так :( (Паролі не співпадають)")

    return render(request, 'registration.html')


def authentication(request):
    if 'Authentication' in request.POST:
        login = request.POST['log']
        passname = request.POST['pass']
        with open("portal/log_sign.json", "r") as my_file:
            signer_json = my_file.read()
        signer = json.loads(signer_json)
        if "user_" + login in [key for key in signer['REGISTER']['LOGIN_INFO'].keys()] and signer['REGISTER']['LOGIN_INFO']["user_" + login] == {login: passname}:
            return render(request, 'index.html')
        else:
            return HttpResponse("Щось пішло не так :( (Неправильний логін або пароль)")



        # return redirect('main/')
    return render(request, 'authentication.html')

def index(request):
    return render(request, 'index.html')




