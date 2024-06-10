from django.shortcuts import render,redirect
from Backend.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from webapp.models import contactdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def intro(request):
    return render(request,"index.html")

def ad_category(request):
    return render(request,"ad_category.html")
def save_category(request):
    if request.method=="POST":
        na=request.POST.get('cname')
        de=request.POST.get('cdesc')
        im=request.FILES['cimage']
        obj=categorydb(CName=na,CDesc=de,CImage=im)
        obj.save()
        messages.success(request,"Category Added Successfully")
        return redirect(ad_category)
def cat_display(request):
    data=categorydb.objects.all()
    return render(request,"cdisplay.html",{'data':data})

def cat_edit(request,catid):
    cat=categorydb.objects.get(id=catid)
    return render(request,"cat_edit.html",{'cat':cat})

def cat_update(request,catid):
    if request.method=="POST":
        na = request.POST.get('cname')
        de = request.POST.get('cdesc')
        try:
            im=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=catid).CImage
        categorydb.objects.filter(id=catid)
        messages.success(request, "Category updated successfully")
        return redirect(cat_display())

def cat_delete(request,catid):
    x=categorydb.objects.filter(id=catid)
    x.delete()
    messages.success(request,"Category deleted successfully")
    return redirect(cat_display)

def ad_product(request):
    cat=categorydb.objects.all()
    return render(request,"ad_products.html",{'cat':cat})

def save_product(request):
    if request.method=="POST":
        cn=request.POST.get('cat')
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        pd=request.POST.get('pdesc')
        pim=request.FILES['pimage']
        obj=productdb(Category=cn,PName=pn,Price=pr,PDesc=pd,PImage=pim)
        obj.save()
        messages.success(request, "Product Added Successfully")
        return redirect(ad_product)

def pro_display(request):
    data=productdb.objects.all()
    return render(request,"pdisplay.html",{'data':data})

def pro_edit(request,proid):
    pro=productdb.objects.get(id=proid)
    cat = categorydb.objects.all()
    return render(request,"pro_edit.html",{'pro':pro,'cat':cat})

def pro_update(request,proid):
    if request.method == "POST":
        cn = request.POST.get('cat')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        pd = request.POST.get('pdesc')
        try:
            pim = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(pim.name, pim)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=proid).PImage
        productdb.objects.filter(id=proid)
        return redirect(pro_display())

def pro_delete(request,proid):
    x=productdb.objects.filter(id=proid)
    x.delete()
    messages.success(request,"Product deleted successfully")

    return redirect(pro_display)

def con_display(request):
    data=contactdb.objects.all()
    return render(request,"con_display.html",{'data':data})

def con_edit(request):
    return render(request,"con_edit.html")

def login_page(request):
    return render(request,"admin_login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pw=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pw)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['pass']=pw
                messages.success(request,"Welcome")
                return redirect(intro)
            else:
                messages.warning(request, "Invalid Credentials")
                return redirect(login_page)
        else:
            messages.warning(request, "No user found")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "User deleted Successfully")
    return redirect(login)







