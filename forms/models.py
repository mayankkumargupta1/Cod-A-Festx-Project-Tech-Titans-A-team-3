from django.db import models
from users.models import User
from django.core.validators import RegexValidator
from .utils import *


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# Create your models here.
class Your_problem_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    village_or_town  = models.CharField(max_length=120,null=False, blank=False)
    address = models.TextField(null=False, blank=False)

    issue_is_related_to = models.TextField(max_length=300,null=False, blank=False)

    Your_problem_state = models.CharField(max_length=200, null=False, blank=False)
    Your_problem_district = models.CharField(max_length=200,null=False, blank=False)
    Your_problem_block = models.CharField(max_length=120,null=False, blank=False)
    Your_problem_thana = models.CharField(max_length=120,null=False, blank=False)
    Your_problem_tehsil = models.CharField(max_length=120,null=False, blank=False)
    Your_problem_village_or_town  = models.CharField(max_length=120,null=False, blank=False)
    Your_problem_address = models.TextField(null=False, blank=False)

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)
    
    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Problem Titile: ' + str(self.issue_is_related_to)
    

class Your_suggestion_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    teshil = models.CharField(max_length=120,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    village_or_town  = models.CharField(max_length=120,null=False, blank=False)
    address = models.TextField(null=False, blank=False)

    Your_suggestion_is_related_to = models.TextField(max_length=300,null=False, blank=False)

    message = models.TextField(max_length=300,null=False, blank=False)
    description = models.TextField(max_length=300,null=False, blank=False)

    vedio = models.URLField(null=True, blank=True)

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Suggestion Title: ' + str(self.Your_suggestion_is_related_to)


class doctors_panel_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_doctor = models.CharField(max_length=200)
    graduation_course = models.TextField(max_length=300,null=False, blank=False)
    post_graduation_course = models.TextField(max_length=300,null=False, blank=False)
    diploma = models.CharField(max_length=300)
    specialization = models.CharField(max_length=300)

    Accademic_details = models.TextField(max_length=300,null=False, blank=False)


    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    
    clinic_address = models.TextField(null=False, blank=False)

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Doctors Name: ' + str(self.name_of_doctor)
    
class hospital_panel_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_hospital = models.CharField(max_length=200)
    hospital_address = models.TextField(max_length=800,null=False, blank=False)
    name_of_manager = models.CharField(max_length=200)

    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    
    free_facility = models.CharField(max_length=200, null=True, blank=True)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Hospital Name: ' + str(self.name_of_hospital)
    
class judicial_help_panel_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_advocate = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=200)
    Specialization = models.CharField(max_length=200)
    name_of_court = models.CharField(max_length=200)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    
    chamber_address = models.TextField(max_length=800,null=False, blank=False)

    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Advocate Name: ' + str(self.name_of_advocate)
    

class Plantation_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_plantation = models.CharField(max_length=200)
    name_of_planters = models.CharField(max_length=200)
    address_of_plantation = models.TextField(max_length=800,null=False, blank=False)

    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    no_of_plantation_plant = models.IntegerField()

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Planters Name: ' + str(self.name_of_planters)
    
    
class Save_water_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_complain = models.CharField(max_length=200)
    complainers = models.CharField(max_length=200)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    
    address = models.TextField(max_length=800,null=False, blank=False)
    date_of_work = models.CharField(max_length=200)
    date_of_report = models.CharField(max_length=200)
    working_organization = models.CharField(max_length=200)
    
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    no_of_plantation_plant = models.IntegerField()

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Complainers Name: ' + str(self.complainers)


class arogya_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_help = models.CharField(max_length=200)
    name_of_patient = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    diseases = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)

    free_facility = models.CharField(max_length=200)
    falicitator = models.CharField(max_length=200)
    

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Patient Name: ' + str(self.name_of_patient)


class Clean_India_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_complain = models.CharField(max_length=200)
    complainers = models.CharField(max_length=200)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    
    address = models.TextField(max_length=800,null=False, blank=False)
    date_of_work = models.CharField(max_length=200)
    date_of_report = models.CharField(max_length=200)
    working_organization = models.CharField(max_length=200)
    
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)

    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Complainers Name: ' + str(self.complainers)
    

class Rakt_veer_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#  details of blood donor
    name_of_donor = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    blood_group = models.CharField(max_length=200)
    date_of_donation = models.CharField(max_length=200)
    
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)


#  details of blood receiver
    name_of_hospital = models.CharField(max_length=200)
    
    address_of_hospital = models.CharField(max_length=200)
    Rstate = models.CharField(max_length=200, null=False, blank=False)
    Rdistrict = models.CharField(max_length=200,null=False, blank=False)
    Rblock = models.CharField(max_length=120,null=False, blank=False)
    Rthana = models.CharField(max_length=120,null=False, blank=False)
    Rtehsil = models.CharField(max_length=120,null=False, blank=False)


    Rmobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    name_of_patient = models.CharField(max_length=200)
    Rblood_group = models.CharField(max_length=200)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Donors Name: ' + str(self.name_of_donor)

class judicial_help_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField(max_length=800,null=False, blank=False)
    gender = models.CharField(max_length=200)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    
    name_of_court = models.CharField(max_length=200)
    district_of_court = models.CharField(max_length=200,null=False, blank=False)
    name_of_advocate = models.CharField(max_length=200)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Help Given to: ' + str(self.name)



class kanya_daan_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_beneficiary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    Fathers_name = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)
    Date_of_marriage = models.CharField(max_length=200)

    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    help_by = models.CharField(max_length=200)
    adhar_no = models.CharField(max_length=200)

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Help Given to: ' + str(self.name_of_beneficiary)


class shiksha_sankalp_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_student_or_school = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)
    class_of_student = models.IntegerField()

    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)


    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)

    donated_item = models.CharField(max_length=200)
    total_no_of_beneficiery = models.CharField(max_length=200)

    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Help Given to: ' + str(self.name_of_student_or_school)
    

class Employment_generation_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name_of_beneficiery = models.CharField(max_length=200)
    age = models.IntegerField()
    DOB = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)
    work_place = models.CharField(max_length=200)
    type_of_work = models.CharField(max_length=200)

    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    salary_income = models.IntegerField()
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Name of Beneficiary: ' + str(self.name_of_beneficiery)
    

class Road_safety_awareness_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_awarness = models.CharField(max_length=200)
    name_of_organizer = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)
    name_of_school_or_student = models.CharField(max_length=200)
    people_participated = models.IntegerField()
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Name of Organizer: ' + str(self.name_of_organizer)
    

class Cancer_awareness_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_awarness = models.CharField(max_length=200)
    name_of_organizer = models.CharField(max_length=200)
    address = models.TextField(max_length=800,null=False, blank=False)
    name_of_school_or_student = models.CharField(max_length=200)
    people_participated = models.IntegerField()
    state = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=200,null=False, blank=False)
    block = models.CharField(max_length=120,null=False, blank=False)
    thana = models.CharField(max_length=120,null=False, blank=False)
    tehsil = models.CharField(max_length=120,null=False, blank=False)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Username ' +str(self.user.username) + ' Name of Beneficiary: ' + str(self.name_of_beneficiery)
    

class Volunteer_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Fathers_name = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    
    # local address
    Lstate = models.CharField(max_length=200, null=False, blank=False)
    Ldistrict = models.CharField(max_length=200,null=False, blank=False)
    Lblock = models.CharField(max_length=120,null=False, blank=False)
    Lthana = models.CharField(max_length=120,null=False, blank=False)
    Ltehsil = models.CharField(max_length=120,null=False, blank=False)
    Laddress = models.TextField(max_length=800,null=False, blank=False)
    
    # permanent address
    Pstate = models.CharField(max_length=200, null=False, blank=False)
    Pdistrict = models.CharField(max_length=200,null=False, blank=False)
    Pblock = models.CharField(max_length=120,null=False, blank=False)
    Pthana = models.CharField(max_length=120,null=False, blank=False)
    Ptehsil = models.CharField(max_length=120,null=False, blank=False)
    Paddress = models.TextField(max_length=800,null=False, blank=False)
    
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    whatsapp_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    
    Aadhar_no = models.IntegerField()
    Job_Profile = models.CharField(max_length=200)
    Profession = models.CharField(max_length=200)
    Work_experience_in_Ngo = models.CharField(max_length=200)
    
    document = models.URLField(default=None, null=True, blank=True)
    picture = models.URLField(default=None, null=True, blank=True)

    STATUS = (
        ('Uploaded', 'Uploaded'),
        ('Approved', 'Aproved'),
    )
    status = models.CharField(choices=STATUS, max_length=100)

    def __str__(self):
        return 'Name of Volunteer: ' +str(self.user.username) + ' STATUS: ' + str(self.status)
    



