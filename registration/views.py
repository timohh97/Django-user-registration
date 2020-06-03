from django.shortcuts import render
from .forms import *
from .models import User



def validateForm(request):
    if request.method == 'POST':

        usernameFormObject = usernameForm(request.POST)
        passwordFormObject = passwordForm(request.POST)
        repeatPasswordFormObject = repeatPasswordForm(request.POST)

        if usernameFormObject.is_valid() and passwordFormObject.is_valid():

            usernameData =  usernameFormObject["username"].value()
            passwordData =  passwordFormObject["password"].value()
            repeatPasswordData = repeatPasswordFormObject["repeatPassword"].value()

            if(passwordData==repeatPasswordData):
                if(not checkIfUsernameExists(usernameData)):

                    insertUserIntoDatabase(usernameData,passwordData)
                    return render(request, "success.html")

                else:
                    return render(request, "usernameExists.html")
            else:
                return render(request, "errorInfo.html")




    else:
        usernameFormObject = usernameForm()
        passwordFormObject = passwordForm()
        repeatPasswordFormObject = repeatPasswordForm()

    return render(request, 'index.html',
                  {'usernameInput': usernameFormObject,
                   "passwordInput":passwordFormObject,
                   "repeatPasswordInput":repeatPasswordFormObject})


def checkIfUsernameExists(username):

    if(User.objects.filter(username=username)):
            return True

    return False

def getJsonObjectsInDatabase():

    print(list(User.objects.values()))
    return list(User.objects.values())


def insertUserIntoDatabase(username,password):

    newuser = User(username=username,password=password)

    newuser.save()



def showLogin(request):
     if request.method=='POST':
        usernameFormObject = usernameForm(request.POST)
        passwordFormObject = passwordForm(request.POST)

        if usernameFormObject.is_valid() and passwordFormObject.is_valid():
            usernameData = usernameFormObject["username"].value()
            passwordData = passwordFormObject["password"].value()

            if(validateLoginData(usernameData,passwordData)):
                return render(request, "loginsuccess.html")

            else:
                return render(request,"loginfail.html")


     else:
      usernameFormObject = usernameForm()
      passwordFormObject = passwordForm()

     return render(request,"login.html",{'usernameInput': usernameFormObject,
                   "passwordInput":passwordFormObject})


def validateLoginData(username,password):

    jsonObjects = getJsonObjectsInDatabase()

    for element in jsonObjects:
      if element["username"]==username and element["password"]==password:
            return True

    return False


def resetDatabase(request):
    users = User.objects.all()

    users.delete()

    return render(request, "reset.html")



