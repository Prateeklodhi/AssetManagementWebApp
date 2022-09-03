from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import AssetForms, EmployeeForm
from .models import Asset, Employee
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    assets = Asset.objects.all()
    alloted = Asset.objects.filter(asset_status='Alloted').count()
    unalloted = Asset.objects.filter(asset_status='Unalloted').count()
    assetcount = assets.count()
    employees = Employee.objects.all()
    doctors = Employee.objects.filter(employee_type='Doctor').count()
    technical = Employee.objects.filter(
        employee_type='Technical Helpdesk').count()
    helpdesk = Employee.objects.filter(employee_type='Helpdesk').count()
    mis = Employee.objects.filter(
        employee_type='Management Information System').count()
    dic = {
        'doctors': doctors,
        'technical': technical,
        'helpdesk': helpdesk,
        'mis': mis,
        'assetcount': assetcount,
        'assets': assets,
        'employees': employees,
        'alloted': alloted,
        'unalloted': unalloted,
    }
    return render(request, "html/dashboard.html", dic)


@login_required(login_url='login')
def register(request):
    # if request.user.is_authenticated:
    #     return redirect('asset')
    # else:
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save
        user = form.cleaned_data.get('username')
        messages.success(request,'Account created for '+user)
        return redirect(request,'login')
    dic = {
        'form':form
    }
    return render(request,"html/register.html",dic)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('asset')
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password = request.POST.get('password')
            userdata = authenticate(request,username = username,password = password  )
            if userdata is not None:
                login(request,userdata)
                return redirect('dashboard')
            else:
                messages.info(request,"Username or password might be incorrect")
        return render(request,'html/login.html')


def logoutUser(request):
    logout(request)
    return redirect('dashboard')

@login_required(login_url='login')
def getasset(request):  
    query = request.GET.get('query') if request.GET.get('query') != None else ''
    print(query)
    assets = Asset.objects.filter(
        Q(asset_name__icontains=query)|
        Q(asset_host_id__icontains=query)|
        Q(issued_to__name__startswith =query)|
        Q(asset_status__startswith=query)
        )
    form = AssetForms()
    if request.method == "POST":
        form = AssetForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assets')
        form = AssetForms()
    dic = {
        'assets':assets,
        'form':form,
    }
    return render(request,'html/index.html',dic)

@login_required(login_url='login')
def showasset(request,assetid):
    asset = Asset.objects.get(asset_serial_number = assetid)
    form=AssetForms(instance=asset)
    if request.method == "POST":
        form = AssetForms(request.POST,request.FILES,instance=asset)
        if form.is_valid():
            form.save()
            return redirect ('assets')
    dic = {
        'asset':asset,
        'form':form,
    }
    return render(request,'html/assetupdate.html',dic)

@login_required(login_url='login')
def deleteasset(request,assetid):
    asset = Asset.objects.get(asset_serial_number= assetid)
    form = AssetForms()   
    if request.method =="POST":
        asset.delete()
        return redirect('assets')
    dic ={
        'asset':asset,
        'form':form,
    }     
    return render(request,'html/asset_delete.html',dic)

@login_required(login_url='login')
def addemployee(request):
    employees = Employee.objects.all()
    forms = EmployeeForm()
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    dic={
        'forms':forms,
        'employees':employees,
    }
    return render(request,'html/employees.html',dic)

@login_required(login_url='login')
def deleteEmployee(request,pk):
    employee =Employee.objects.get(employee_id = pk)
    if request.method =='POST':
        employee.delete()
        return redirect('employees')
    dic ={
        'employee':employee,
    }
    return render(request,'html/deleteemployee.html',dic)