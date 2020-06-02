from django.shortcuts import render
from .forms import *
import pymongo
from bson import ObjectId
from pymongo import MongoClient
import bcrypt
import requests
import pprint



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


    listOfJsonObjectsInCollection = getListOfJsonObjects()

    for element in listOfJsonObjectsInCollection:
        if(element["username"]==username):
            return True

    return False



def getListOfJsonObjects():
    request = requests.get('https://pythonapi.netlify.app/.netlify/functions/api')
    print(request.json())

    return request.json()




def insertUserIntoDatabase(username,password):

    byteStringPassword = password.encode("utf-8")

    hashedPassword = bcrypt.hashpw(byteStringPassword,bcrypt.gensalt())

    json = {"username":username,"password":hashedPassword}

    request = requests.post('https://pythonapi.netlify.app/.netlify/functions/api',data=json)


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
    listOfJsonObjectsInCollection=getListOfJsonObjects()

    byteStringPassword = password.encode("utf-8")

    for element in listOfJsonObjectsInCollection:
        if(element["username"]==username and bcrypt.checkpw(byteStringPassword,element["password"].encode("utf-8"))):
            return True

    return False




