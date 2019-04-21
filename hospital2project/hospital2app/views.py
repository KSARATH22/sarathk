from django.shortcuts import render
from.models import Doctors,Patients,Nurses,Reports,Messages,ContactData,FeedbackData
from.forms import DocterForm,PatientsForm,NursesForm,ReportsForm,MessagesForm,ContactForm,FeedbackForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'Hoshome.html')
def doctors(request):
    if request.method =="POST":
        dform=DocterForm(request.POST)
        if dform.is_valid():
            fname=request.POST.get('first_name','')
            lname=request.POST.get('last_name','')
            email1=request.POST.get('email','')
            mobile1=request.POST.get('mobile','')
            addres1=request.POST.get('addres','')


            data=Doctors(
                first_name=fname,
                last_name=lname,
                email=email1,
                mobile=mobile1,
                addres=addres1,
            )
            data.save()
            dform=DocterForm()
            return render(request,'HosDoctor.html',{'dform':dform})
        else:
            return HttpResponse('form is not valid')
    else:
        dform = DocterForm()
        return render(request, 'HosDoctor.html', {'dform': dform})
import  datetime
time1 = datetime.datetime.now()

def patients(request):
    if request.method == "POST":
        pform=PatientsForm(request.POST)
        if pform.is_valid():
            fname=request.POST.get('first_name','')
            lname=request.POST.get('last_name','')
            pa=request.POST.get('pat_age',''),
            pg=request.POST.get('pat_gender','')
            mobile1=request.POST.get('mobile','')
            addres1=request.POST.get('addres','')

            data=Patients(
                first_name=fname,
                last_name=lname,
                pat_age=pa,
                pat_gender=pg,
                mobile=mobile1,
                addres=addres1,
            )
            data.save()
            pform=PatientsForm()
            return render(request,'Hospatient.html',{'pform':pform})
        else:
            return HttpResponse('form is not valid')
    else:
        pform = PatientsForm()
        return render(request, 'Hospatient.html', {'pform': pform})
def nurses(request):
    if request.method == "POST":
        nform=NursesForm(request.POST)
        if nform.is_valid():
            fname2=request.POST.get('first_name','')
            lname2=request.POST.get('last_name','')
            email=request.POST.get('email','')
            addres2=request.POST.get('addres','')

            data=Nurses(
                first_name=fname2,
                last_name=lname2,
                email=email,
                addres=addres2,
            )
            data.save()
            nform=NursesForm()
            return render(request,'Hosnurse.html',{'nform':nform})
        else:
            return HttpResponse('form is not valid')
    else:
        nform = NursesForm()
        return render(request, 'Hosnurse.html', {'nform': nform})
import  datetime
time1 = datetime.datetime.now()

def reports(request):
    if request.method=="POST":
        rform=ReportsForm(request.POST)
        if rform.is_valid():
            case1=request.POST.get('case','')
            lab_a=request.POST.get('lab_attendant','')

            des=request.POST.get('description','')
            data=Reports(
                case=case1,
                lab_attendant=lab_a,

                description=des,
            )
            data.save()
            rform=ReportsForm()
            return render(request,'Hosreport.html',{'rform':rform})
        else:
            return HttpResponse('form is not valid')
    else:
        rform = ReportsForm()
        return render(request, 'Hosreport.html', {'rform': rform})

def messages(request):
    if request.method =="POST":
        mform=MessagesForm(request.POST)
        if mform.is_valid():
            name1=request.POST.get('name','')
            dt1=request.POST.get('datetime','')
            mess=request.POST.get('message','')
            rating2=request.POST.get('rating','')
            data=Messages(
                name=name1,
                datetime=dt1,
                message=mess,
                rating=rating2,
            )
            data.save()
            mform=MessagesForm()
            return render(request,'Hosmessage.html',{'mform':mform})
        else:
            return HttpResponse('form is not valid')
    else:
        mform = MessagesForm()
        return render(request, 'Hosmessage.html', {'mform': mform})
def contact(request):
    if request.method=="POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            fname=request.POST.get('first_name','')
            lname=request.POST.get('last_name','')
            email1=request.POST.get('email','')
            mobile1=request.POST.get('mobile','')
            data=ContactData(
                first_name=fname,
                last_name=lname,
                email=email1,
                mobile=mobile1,

            )
            data.save()
            cform=ContactForm()
            return render(request,'Hoscontact.html',{'cform':cform})
        else:
            return HttpResponse('form is not valid')
    else:
        cform = ContactForm()
        return render(request, 'Hoscontact.html', {'cform': cform})


import datetime as dt
date1 = dt.datetime.now()
def feedback(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            feedback = request.POST.get('feedback','')

            name = name.capitalize()

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                time=date1
            )
            data.save()
            fbdata = FeedbackData.objects.all()
            fform = FeedbackForm()
            return render(request,'Hosfeedback.html',{'fform':fform})


    else:
        fbdata = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request,'Hosfeedback.html',{'fform':fform, 'fbdata':fbdata})


def gellery(request):
    return render(request,'Hosgellery.html')








































