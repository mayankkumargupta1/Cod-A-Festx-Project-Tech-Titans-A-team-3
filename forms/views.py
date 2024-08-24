from django.shortcuts import render, redirect
from .models import *
from .utils import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Home.models import Navigation_link

@login_required
def Your_problem(request):
    if request.method == 'POST':
        issue_is_related_to = request.POST.get('issue_is_related_to')
        other_issue_text = request.POST.get('other_issue_text', '')
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None
        try:
            data = Your_problem_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = Your_problem_form(
                user=request.user,
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                state=request.POST['state'],
                district=request.POST['district'],
                teshil=request.POST['tehsil'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                village_or_town=request.POST['village_or_town'],
                address=request.POST['address'],
                issue_is_related_to=issue_is_related_to if issue_is_related_to != 'Other' else other_issue_text,
                Your_problem_state=request.POST['Your_problem_state'],
                Your_problem_district=request.POST['Your_problem_district'],
                Your_problem_teshil=request.POST['Your_problem_teshil'],
                Your_problem_block=request.POST['Your_problem_block'],
                Your_problem_thana=request.POST['Your_problem_thana'],
                Your_problem_tehsil=request.POST['Your_problem_tehsil'],
                Your_problem_village_or_town=request.POST['Your_problem_village_or_town'],
                Your_problem_address=request.POST['Your_problem_address'],
                
                document=up_document,
                picture=up_photo,
                status = 'Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')
    
    
    nav_link = Navigation_link.objects.all()
    
    context = {
        'Navigation_link' : nav_link,
        
    }
    return render(request, 'forms/your_problem.html', context=context)

@login_required
def Your_suggestion(request):
    
    if request.method == 'POST':
        issue_is_related_to = request.POST.get('issue_is_related_to')
        other_issue_text = request.POST.get('other_issue_text', '')
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None
        try:
            data = Your_suggestion_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = Your_suggestion_form(
                user=request.user,
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                state=request.POST['state'],
                district=request.POST['district'],
                teshil=request.POST['tehsil'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                village_or_town=request.POST['village_or_town'],
                address=request.POST['address'],
                Your_suggestion_is_related_to=issue_is_related_to if issue_is_related_to != 'Other' else other_issue_text,
                message = request.POST['message'],
                description = request.POST['description'],
                vedio = request.POST['video'],                
                document=up_document,
                picture=up_photo,
                status = 'Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')


    nav_link = Navigation_link.objects.all()
    context = {
        'Navigation_link' : nav_link,
    }
    return render(request, 'forms/your_suggestion.html', context=context)



@login_required
def doctors_panel(request):
    if request.method == 'POST':
        graduation_course = request.POST.get('graduation_course')
        graduation_course_other = request.POST.get('graduation_course_other', '')
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None
        try:
            data = doctors_panel_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = doctors_panel_form(
                user=request.user,
                name_of_doctor = request.POST['doctor-name'],
                graduation_course = graduation_course if graduation_course != 'Other' else graduation_course_other,
                post_graduation_course = request.POST['post_graduation'],
                diploma = request.POST['diploma'],
                specialization = request.POST['specialization'],
                Accademic_details = request.POST['academic-details'],


                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                
                clinic_address=request.POST['address'],
                
                document=up_document,
                picture=up_photo,
                status = 'Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')


    nav_link = Navigation_link.objects.all()
    context = {
        'Navigation_link' : nav_link,
    }
    return render(request, 'forms/doctors_panel.html', context=context)

@login_required
def hospital_panel(request):
    if request.method == 'POST':
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None
        try:
            data = hospital_panel_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = hospital_panel_form(
                user=request.user,
                name_of_hospital = request.POST['name_of_hospital'],
                hospital_address = request.POST['hospital_address'],
                name_of_manager = request.POST['name_of_manager'],
                        
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                
                free_facility = request.POST['free_facility'],

                document=up_document,
                picture=up_photo,
                status = 'Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')


    nav_link = Navigation_link.objects.all()
    context = {
        'Navigation_link' : nav_link,
    }
    return render(request, 'forms/hospital_panel.html', context=context)

from payments import models as pay
from django.urls import reverse
from django.shortcuts import get_object_or_404
@login_required
def Volunteer_panel(request):
    if request.method == 'POST':
        if pay.payment.objects.filter(user= request.user).exists() == False:
            return redirect(reverse('payments:create_order'))
        else:
            issue_is_related_to = request.POST.get('Profession')
            other_issue_text = request.POST.get('other_profession', '')
            up_document = request.FILES.get('document')
            
            if up_document is not None:
                up_document = file_url(up_document)
            else:
                up_document = None
            
            up_photo = request.FILES.get('picture')
            if up_photo is not None:
                up_photo = image_url(up_photo)
            else:
                up_photo = None

            try:
                data = Volunteer_form.objects.filter(user=request.user)
            except:
                data = ''
            
            if len(data) < 1:
                form = Volunteer_form(
                    user=request.user,

                    Fathers_name = request.POST['Fathers_name'],
                    DOB = request.POST['DOB'],
                    Gender = request.POST['Gender'],
                    
                    # local address
                    Lstate = request.POST['Lstate'],
                    Ldistrict = request.POST['Ldistrict'],
                    Lblock = request.POST['Lblock'],
                    Lthana = request.POST['Lthana'],
                    Ltehsil = request.POST['Ltehsil'],
                    Laddress = request.POST['Laddress'],
                    
                    # permanent address
                    Pstate = request.POST['Pstate'],
                    Pdistrict = request.POST['Pdistrict'],
                    Pblock = request.POST['Pblock'],
                    Pthana = request.POST['Pthana'],
                    Ptehsil = request.POST['Ptehsil'],
                    Paddress = request.POST['Paddress'],
                    
                    mobile_number = request.POST['mobile_number'],
                    whatsapp_number = request.POST['whatsapp'],
                    
                    Aadhar_no = request.POST['Aadhar_no'],
                    Job_Profile = request.POST['Job_Profile'],
                    Profession = issue_is_related_to if issue_is_related_to != 'Other' else other_issue_text,
                    Work_experience_in_Ngo = request.POST['Work_experience_in_Ngo'],

                    document=up_document,
                    picture=up_photo,
                    status = 'Uploaded'
                )
                form.save()
                messages.success(request,'Application saved')
                return redirect('/')  
            else:
                instance = get_object_or_404(Volunteer_form, user = request.user)
                instance.Fathers_name = request.POST['Fathers_name']
                instance.DOB = request.POST['DOB']
                instance.Gender = request.POST['Gender']
                
                # local address
                instance.Lstate = request.POST['Lstate']
                instance.Ldistrict = request.POST['Ldistrict']
                instance.Lblock = request.POST['Lblock']
                instance.Lthana = request.POST['Lthana']
                instance.Ltehsil = request.POST['Ltehsil']
                instance.Laddress = request.POST['Laddress']
                
                # permanent address
                instance.Pstate = request.POST['Pstate']
                instance.Pdistrict = request.POST['Pdistrict']
                instance.Pblock = request.POST['Pblock']
                instance.Pthana = request.POST['Pthana']
                instance.Ptehsil = request.POST['Ptehsil']
                instance.Paddress = request.POST['Paddress']
                
                instance.mobile_number = request.POST['mobile_number']
                instance.whatsapp_number = request.POST['whatsapp']
                
                instance.Aadhar_no = request.POST['Aadhar_no']
                instance.Job_Profile = request.POST['Job_Profile']
                instance.Profession = issue_is_related_to if issue_is_related_to != 'Other' else other_issue_text
                instance.Work_experience_in_Ngo = request.POST['Work_experience_in_Ngo']

                instance.document=up_document
                instance.picture=up_photo
                instance.save()
                messages.success(request,'Application Updated')
                return redirect('/')

    if request.method == 'GET':
        if pay.payment.objects.filter(user= request.user).exists() == False:
                return redirect(reverse('payments:create_order'))
        else:
            nav_link = Navigation_link.objects.all()
            context = {
                'Navigation_link' : nav_link,
            }
            return render(request, 'forms/volunteer.html', context=context)

@login_required
def arogya_yojana(request):
    if request.method == 'POST':
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None

        try:
            data = arogya_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = arogya_form(
                user=request.user,
                date_of_help=request.POST['date_of_help'],
                name_of_patient=request.POST['name_of_patient'],
                gender=request.POST['gender'],
                diseases=request.POST['diseases'],
                address=request.POST['address'],
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                free_facility=request.POST['free_facility'],
                falicitator=request.POST['falicitator'],
                document=up_document,
                picture=up_photo,
                status='Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')
    
    nav_link = Navigation_link.objects.all()
    
    context = {
        'Navigation_link': nav_link,
    }
    return render(request, 'forms/arogya_yojana.html', context=context)


@login_required
def judicial_help_panel(request):
    if request.method == 'POST':
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None

        try:
            data = judicial_help_panel_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = judicial_help_panel_form(
                user=request.user,
                name_of_advocate=request.POST['name_of_advocate'],
                Qualification=request.POST['Qualification'],
                Specialization=request.POST['Specialization'],
                name_of_court=request.POST['name_of_court'],
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                chamber_address=request.POST['chamber_address'],
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                document=up_document,
                picture=up_photo,
                status='Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')
    
    nav_link = Navigation_link.objects.all()
    
    context = {
        'Navigation_link': nav_link,
    }
    return render(request, 'forms/judicial_help_panel.html', context=context)


@login_required
def plantation(request):
    if request.method == 'POST':
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None

        try:
            data = Plantation_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = Plantation_form(
                user=request.user,
                date_of_plantation=request.POST['date_of_plantation'],
                name_of_planters=request.POST['name_of_planters'],
                address_of_plantation=request.POST['address_of_plantation'],
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                no_of_plantation_plant=request.POST['no_of_plantation_plant'],
                document=up_document,
                picture=up_photo,
                status='Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')
    
    nav_link = Navigation_link.objects.all()
    
    context = {
        'Navigation_link': nav_link,
    }
    return render(request, 'forms/plantation.html', context=context)



@login_required
def save_water(request):
    if request.method == 'POST':
        up_document = request.FILES.get('document')
        
        if up_document is not None:
            up_document = file_url(up_document)
        else:
            up_document = None
        
        up_photo = request.FILES.get('picture')
        if up_photo is not None:
            up_photo = image_url(up_photo)
        else:
            up_photo = None

        try:
            data = Save_water_form.objects.filter(user=request.user)
        except:
            data = ''
        
        if len(data) <= 5:
            form = Save_water_form(
                user=request.user,
                date_of_complain=request.POST['date_of_complain'],
                complainers=request.POST['complainers'],
                mobile_number=request.POST['mobile_number'],
                whatsapp=request.POST['whatsapp'],
                address=request.POST['address'],
                date_of_work=request.POST['date_of_work'],
                date_of_report=request.POST['date_of_report'],
                working_organization=request.POST['working_organization'],
                state=request.POST['state'],
                district=request.POST['district'],
                block=request.POST['block'],
                thana=request.POST['thana'],
                tehsil=request.POST['tehsil'],
                no_of_plantation_plant=request.POST['no_of_plantation_plant'],
                document=up_document,
                picture=up_photo,
                status='Uploaded'
            )
            form.save()
            return redirect('/')  
        else:
            messages.error(request, 'YOU HAVE REACHED THE MAXIMUM ALLOWED FORM SUBMISSION LIMIT WHICH IS 5')
            return redirect('/')
    
    nav_link = Navigation_link.objects.all()
    
    context = {
        'Navigation_link': nav_link,
    }
    return render(request, 'forms/save_water.html', context=context)