from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app1.forms import empForm
from app1.forms import newsForm
from app1.forms import holidayForm
from app1.models import emp,News,holiday
from django.http import HttpResponse
import csv


# Create your views here.

def home_view(request):
	return render(request,'app1/home.html')

@login_required
def hrmgr_view(request):
	return render(request,'app1/hr_mgr.html')

def employee_view(request):
	return render(request,'app1/employee.html')


def addemp_view(request):
	form=empForm()
	if request.method=="POST":
		form=empForm(request.POST)

		if form.is_valid():
			form.save()
			return viewemp_view(request)
	return render(request,'app1/addemp.html', {'form':form})

def viewemp_view(request):
	EMP = emp.objects.all()
	return render(request,'app1/viewemp.html', {'emp':EMP})


def calender_view(request):
	form=holidayForm()
	if request.method=='POST':
		form=holidayForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/holiday')

	return render(request,'app1/calender.html',{'form':form})

def delete_view(request, id):
	employee=emp.objects.get(id=id)
	employee.delete()
	return redirect(viewemp_view)

def update_view(request,id):
	employee=emp.objects.get(id=id)
	if request.method=="POST":
		form=empForm(request.POST, instance=employee) #instance=employee means replacing existing record
		if form.is_valid():
			form.save()
		return redirect('/view_emp') #redirecting to results page like sample.html
	return render(request,'app1/update.html',{'employee':employee})


def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = emp.objects.all()  
    writer = csv.writer(response)  
    writer.writerow(['EmpName', 'EID', 'DESIGNATION', 'JOININGDATE', 'DEPARTMENT', 'SALARAY', 'EXPERIENCE'])
    for i in employees:  
        writer.writerow([i.eName, i.eID, i.eDesignation, i.eJoiningDate, i.eDepartment, i.eSalary, i.eExperience])  
    return response  

def newsshow_view(request):
	news = News.objects.all()
	return render(request,'app1/newsshow.html', {'news':news})

def holiday_view(request):
	holidays = holiday.objects.all()
	return render(request,'app1/holiday.html', {'holidays':holidays})


def latestnews_view(request):
    form=newsForm()

    if request.method=='POST':
        form=newsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/news')

    return render(request,'app1/latestnews.html',{'form':form})


