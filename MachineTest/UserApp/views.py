from django.shortcuts import render,redirect
from UserApp.models import UserInfo
from django.contrib import messages
# Create your views here.
def Signup(request):
    if(request.method=="GET"):
        return render(request,"Signup.html",{})
    else:
        id=request.POST["id"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        email=request.POST["email"]
        phone_number=request.POST["phoneno"]
        role=request.POST["role"]
        
        #Already Exist
        try:
            user=UserInfo.objects.get(username=uname)
        except:
            user=UserInfo(id,fname,lname,email,uname,pwd,phone_number,role)
            user.save()
        else:
            messages.error(request,"User Name Already Present!! Please Use another User Name and Password.")
            return redirect(home)
            #return HttpResponse("User Name Already Present")
        request.session["uname"]=uname
        messages.success(request,"Welcome, ")
        if(role=="Vendor"):
            return render(request,"Vendor.html",{})
        else:
            return render(request,"user.html",{})

def home(request):
    if(request.method=="GET"):
        return render(request,"home.html",{})
    else:
        #Check UserName and Password
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        try:
            user=UserInfo.objects.get(username=uname,password=pwd)
        except:
            messages.error(request,"Invalid Credentials!! Please Enter Valid User Name and Password.")
            return redirect(home)

        #usernmae in session
        request.session["uname"]=uname
        messages.success(request,"Welcome Back, ")
        u_role=UserInfo.objects.get(role=UserInfo.objects.get(username=uname))
        if(u_role=="Vendor"):
            return render(request,"Vendor.html",{})
        else:
            return render(request,"user.html",{})

def logout(request):
    request.session.clear()
    return redirect(home)