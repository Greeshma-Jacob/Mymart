from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb
from webapp.models import contactdb,registrationdb,cartdb
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat=categorydb.objects.all()
    return render(request,"home.html",{'cat':cat})

def aboutpage(request):
    cat = categorydb.objects.all()
    return render(request,"about.html",{'cat':cat})

def contactpage(request):
    cat = categorydb.objects.all()
    return render(request,"contact.html",{'cat':cat})

def our_products(request):
    cat = categorydb.objects.all()
    pro=productdb.objects.all()
    return render(request,"our_products.html",{'pro':pro,'cat':cat})

def save_contact(request):
    if request.method== "POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        su=request.POST.get('subject')
        me=request.POST.get('message')

        obj1=contactdb(Name=na,Email=em,Phone=ph,Subject=su,Message=me)
        obj1.save()
        return redirect(contactpage)

def products_filtered(request,cat_name):
    cat = categorydb.objects.all()
    data = productdb.objects.filter(Category=cat_name)
    return render(request,"products_filtered.html",{'data':data,'cat':cat})

def single(request,pro_id):
    data=productdb.objects.get(id=pro_id)
    return render(request,"singleproducts.html",{'data':data})

def register(request):
    return render(request,"register.html")

def save_register(request):
    if request.method=="POST":
        un=request.POST.get('uname')

        em=request.POST.get('email')
        psw=request.POST.get('pass1')
        cnf=request.POST.get('pass2')

        obj=registrationdb(Username=un,Email=em,Pass=psw,Confirm=cnf)
        if registrationdb.objects.filter(Username=un).exists():
            messages.warning(request,"Username Already Exists...!")
        elif registrationdb.objects.filter(Email=em).exists():
            messages.warning(request,"Mail Id Already Taken...!")
        else:
            obj.save()
            messages.success(request, "Registration Successful...!")
        return redirect(register)

def user_login(request):
    if request.method=="POST":
        us=request.POST.get('username')
        pwd=request.POST.get('password')
        if registrationdb.objects.filter(Username=us,Pass=pwd).exists():
            request.session['Username']=us
            request.session['Pass']=pwd

            messages.success(request, "Successfully Logged In")
            return redirect(homepage)
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect(register)
    else:
        messages.warning(request, "No user found")
        return redirect(register)

def user_logout(request):
    del request.session['Username']
    del request.session['Pass']
    messages.success(request, "Logout Successful")
    return redirect(homepage)

def add_cart(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pn=request.POST.get('pname')
        qu=request.POST.get('quantity')
        tp=request.POST.get('tprice')

        obj=cartdb(UName=un,PName=pn,Quantity=qu,TPrice=tp)
        obj.save()
        messages.success(request,"Item Added To Cart")
        return redirect(homepage)

def cart_page(request):
    cat = categorydb.objects.all()
    data=cartdb.objects.filter(UName=request.session['Username'])
    total=0
    for d in data:
        total=total+d.TPrice
    return render(request,"cart.html",{'data':data,'cat':cat,'total':total})

def delete_item(request,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cart_page)

def member_login(request):
    return render(request,"userlogin.html")

def checkout(request):
    return render(request,"checkout.html")

def payment(request):
    return render(request,"payment.html")





