from django.shortcuts import render,redirect
from services.models import *
from mail.models import *
from services.forms import *
from django.contrib.auth import authenticate,login
import psycopg2
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from reminder.settings import EMAIL_HOST_USER

conn = psycopg2.connect(database="reminder_website", user = "postgres", password = "jigarpinakin", host = "localhost", port = "5432")
cur = conn.cursor()
email_data = 'Hi reminder'
# def home_view(request):
#     return render(request, 'home.html')

def service_data_view(service_name,service_type,date_of_deadline, reminder_before,recurrence_type):
    
    obj = ServiceDateModel(service_name=service_name,service_type=service_type,date_of_deadline=date_of_deadline,actual_date_on_which_reminder_is_to_be_sent = reminder_before,recurrence_type = recurrence_type)
    obj.save()
    obj = ScheduleTaskModel(service_name=service_name,service_type=service_type,date_of_deadline=date_of_deadline,actual_date_on_which_reminder_is_to_be_sent = reminder_before,recurrence_type = recurrence_type,email_data=email_data)
    obj.save()

def incometax_view(request):

    if request.method == 'GET':
        return render(request, 'incometax.html')
    #7 models are getting stored in data_storage
    if(True):
        first_install= request.POST.get('first_install')
        days_before = int(request.POST.get('first_install_reminder_before'))
        first_install_reminder_before = days_before_to_date(first_install,days_before)
        service_data_view('Income Tax','Income tax first installment due date',first_install,first_install_reminder_before,12)
        
        second_install= request.POST.get('second_install')
        days_before = int(request.POST.get('second_install_reminder_before'))
        second_install_reminder_before = days_before_to_date(second_install,days_before)
        service_data_view('Income Tax','Income tax second installment due date',second_install,second_install_reminder_before,12)
        
        third_install= request.POST.get('third_install')
        days_before = int(request.POST.get('third_install_reminder_before'))
        third_install_reminder_before = days_before_to_date(third_install,days_before)
        service_data_view('Income Tax','Income tax third installment due date',third_install,third_install_reminder_before,12)

        fourth_install= request.POST.get('fourth_install')
        days_before = int(request.POST.get('fourth_install_reminder_before'))
        fourth_install_reminder_before = days_before_to_date(fourth_install,days_before)
        service_data_view('Income Tax','Income tax fourth installment due date',fourth_install,fourth_install_reminder_before,12)


        taxreturn= request.POST.get('taxreturn') 
        days_before = int(request.POST.get('tax_return_reminder_before'))
        tax_return_reminder_before = days_before_to_date(taxreturn,days_before)
        service_data_view('Income Tax','Income tax taxreturn due date',taxreturn,tax_return_reminder_before,12)
        
        tdsreturn = request.POST.get('tdsreturn')
        days_before = int(request.POST.get('tds_return_reminder_before'))
        tds_return_reminder_before = days_before_to_date(tdsreturn,days_before)
        service_data_view('Income Tax','Income tax tdsreturn due date',tdsreturn,tds_return_reminder_before,12)
        
        auditreturn = request.POST.get('audit')
        days_before = int(request.POST.get('audit_reminder_before'))
        audit_return_reminder_before = days_before_to_date(auditreturn,days_before)
        service_data_view('Income Tax','Income tax auditreturn due date',auditreturn,audit_return_reminder_before,12)

    # print('Saved')
    return redirect('../')

def durationt_to_rec(duration):
    rec= 0
    if(duration=='monthly'):
        rec =1
    if(duration=='quaterly'):
        rec =3
    if(duration=='half_yearly'):
        rec=6
    if(duration=='yearly'):
        rec=12
    return int(rec) 

def days_before_to_date(curr_date,days_before):
    x,y,z = curr_date.split("-")
    proper_date= date(int(x),int(y),int(z))
    print(proper_date)
    print(type(proper_date))
    # proper_date= datetime.strptime(curr_date, '%y-%m-%d')
    # print("We are printing"*50)
    # print("/n ",proper_date)
    date_before_current_date = proper_date -timedelta(days= days_before)
    return date_before_current_date

def gst_view(request):
    if request.method == 'GET':
        return render(request, 'gst.html')
    print(request.POST)
    print(request.method)
    #date_of_deadline, reminder_before,email,type_of_detail,recurrence_type =1
    duration_1=request.POST.get('duration_1')
    rec_1 = durationt_to_rec(duration_1)
    first_due_GSTR1= request.POST.get('first_due_GSTR1')
    days_before =  int(request.POST.get('first_due_GSTR1_reminder_before'))
    first_due_GSTR1_reminder_before = days_before_to_date(first_due_GSTR1,days_before)
    service_data_view('GST','GSTR1 due date',first_due_GSTR1,first_due_GSTR1_reminder_before,recurrence_type=int(rec_1))

    duration_3=request.POST.get('duration_3')
    rec_3 = durationt_to_rec(duration_3)
    first_due_GSTR3B= request.POST.get('first_due_GSTR3B')
    days_before = int(request.POST.get('first_due_GSTR3B_reminder_before'))
    first_due_GSTR3B_reminder_before = days_before_to_date(first_due_GSTR3B,days_before)
    service_data_view('GST','GSTR3B due date',first_due_GSTR3B,first_due_GSTR3B_reminder_before,recurrence_type=int(rec_3))
    
    annual_return= request.POST.get('annual_return')
    days_before = int(request.POST.get('annual_return_reminder_before'))
    annual_return_reminder_before = days_before_to_date(annual_return,days_before)
    service_data_view('GST','GST annual return due date',annual_return,annual_return_reminder_before,12)
    
    audit_return= request.POST.get('audit')
    days_before = int(request.POST.get('audit_return_reminder_before'))
    audit_return_reminder_before = days_before_to_date(audit_return,days_before)
    service_data_view('GST','GST audit return due date',audit_return,audit_return_reminder_before,12)
    
    print('Saved')
    return redirect('../')
 
def companies_act_view(request):
    if request.method == 'GET':
        return render(request, 'companies_act.html')
    
    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Companies Act','Companies Act Return 1',Return_1,Return_1_reminder_before,12)
    
    Return_2= request.POST.get('Return_2')
    days_before =  int(request.POST.get('Return_2_reminder_before'))
    Return_2_reminder_before = days_before_to_date(Return_2,days_before)
    service_data_view('Companies Act','Companies Act Return 2',Return_2,Return_2_reminder_before,12)

    return redirect('../')

def accounting_view(request):
    if request.method == 'GET':
        return render(request, 'accounting.html')

    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Accounting Act','Accounting Act Return 1',Return_1,Return_1_reminder_before,12)
    
    Return_2= request.POST.get('Return_2')
    days_before =  int(request.POST.get('Return_2_reminder_before'))
    Return_2_reminder_before = days_before_to_date(Return_2,days_before)
    service_data_view('Accounting Act','Accounting Act Return 2',Return_2,Return_2_reminder_before,12)

    # print('Saved')
    return redirect('../')

def other_service1_view(request):
    if request.method == 'GET':
        return render(request, 'other_service1.html')

    duration_1=request.POST.get('duration_1')
    rec_1 = durationt_to_rec(duration_1)
    service_type= request.POST.get('service_type')
    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Other Service 1',service_type,Return_1,Return_1_reminder_before,recurrence_type=int(rec_1))
    # print('Saved')
    return redirect('../')
    
def other_service2_view(request):
    if request.method == 'GET':
        return render(request, 'other_service2.html')

    duration_1=request.POST.get('duration_1')
    rec_1 = durationt_to_rec(duration_1)
    service_type= request.POST.get('service_type')
    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Other Service 2',service_type,Return_1,Return_1_reminder_before,recurrence_type=int(rec_1))
    # print('Saved')
    return redirect('../')
    

def other_service3_view(request):
    if request.method == 'GET':
        return render(request, 'other_service3.html')

    duration_1=request.POST.get('duration_1')
    rec_1 = durationt_to_rec(duration_1)
    service_type= request.POST.get('service_type')
    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Other Service 3',service_type,Return_1,Return_1_reminder_before,recurrence_type=int(rec_1))
    # print('Saved')
    return redirect('../')
    
    
def other_service4_view(request):
    if request.method == 'GET':
        return render(request, 'other_service4.html')

    duration_1=request.POST.get('duration_1')
    rec_1 = durationt_to_rec(duration_1)
    service_type= request.POST.get('service_type')
    Return_1= request.POST.get('Return_1')
    days_before =  int(request.POST.get('Return_1_reminder_before'))
    Return_1_reminder_before = days_before_to_date(Return_1,days_before)
    service_data_view('Other Service 4',service_type,Return_1,Return_1_reminder_before,recurrence_type=int(rec_1))
    # print('Saved')
    return redirect('../')
    

def add_client_view(request):
    if request.method=='GET':
        return render(request,'add_client.html')
    ca_name = None
    
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    query01="SELECT id FROM public.auth_user WHERE username='"+str(username)+"'"
    cur.execute(query01)
    rows=cur.fetchall()
    id = rows[0][0]
    print(id)
    if request.user.is_staff:
        ca_name = request.user.get_full_name()
    
    else:
        query="SELECT ca_name FROM public.authentication_staffmodel WHERE staff_id= %s"
        cur.execute(query,(id,))
        rows=cur.fetchall()
        print(rows)
        ca_name = rows[0][0]
        print("========",ca_name)

    client_type=request.POST.get('client_type')
    print(client_type)
    client_name=request.POST.get('client_name')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    gst=request.POST.get('gst')
    aadhar=request.POST.get('aadhar')
    pan=request.POST.get('pan')
    
    
    income_tax= request.POST.get('check_01')
    gst_tax= request.POST.get('check_02')
    accounting= request.POST.get('check_03')
    companies= request.POST.get('check_04')
    other_service1= request.POST.get('check_05')
    other_service2= request.POST.get('check_06')
    other_service3= request.POST.get('check_07')
    other_service4= request.POST.get('check_08')
    print(accounting,companies,gst_tax,income_tax,other_service1,other_service2,other_service3,other_service4)
    
    print("=="*50)
    print("**"*50)
    
    if(str(income_tax)=='None'):
        income_tax=0
    if(str(gst_tax)=='None'):
        gst_tax=0
    if(str(companies)=='None'):
        companies=0
    if(str(accounting)=='None'):
        accounting=0
    if(str(other_service1)=='None'):
        other_service1=0
    if(str(other_service2)=='None'):
        other_service2=0
    if(str(other_service3)=='None'):
        other_service3=0
    if(str(other_service4)=='None'):
        other_service4=0
        
    # Create user and save to the database
    client = ClientModel(email=email,client_type=client_type,ca_name=ca_name,staff_id=id,client_name=client_name,phone_no=phone,gst=gst,aadhar=aadhar,pan=pan, income_tax_activate=income_tax,gst_tax_activate=gst_tax,
    companies_activate=companies,accounting_activate=accounting,other_service1=other_service1,other_service2=other_service2,other_service3=other_service3,other_service4=other_service4)
    
    client.save()
    
    return redirect('../')

def ca_dashboard_view(request):
    return render(request,'ca_dashboard.html')

def staff_dashboard_view(request):
    return render(request,'staff_dashboard.html')

def client_details_view(request):
    if request.user.is_authenticated:
        ca_name=request.user.get_full_name()
        print(ca_name)
        # f_name,l_name=ca_name.split("  ")
        # ca_name=f_name+" "+l_name
        # print(ca_name)
    query="SELECT * FROM public.services_clientmodel WHERE ca_name='"+str(ca_name)+"'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()

    ###################jigar is commenting##################
    """I am assuming that by default we will show details of all clients
    like it is showing orignally. There will be a dropdown list or radio button
    as perwhich CA can filter clients based on the services enrolled by the clients
    
    Multiple services can be selected and on clicking the submit button the below function of 
    filtering will be called by passing a list of services
    eg: [Income Tax, Companies act]
    Only the users having this two enrolled together will be displayed."""

    ##################jigar ends commenting##########################

    list_of_services=[]
    filer_client_views(list_of_services)
    # print(rows)
    # print(type(rows))
    args={'rows':rows}
    # print(args)
    return render(request,'client_details.html',args)


def delete_client_view(request):
    if request.method == 'GET':
        return render(request, 'delete_client.html')

    emails = request.POST.get('email')
    pan = request.POST.get('pan')
    query_id = "SELECT id FROM public.services_clientmodel WHERE email='"+str(emails)+"' and pan='"+str(pan)+"'"
    cur.execute(query_id)
    rows = cur.fetchall()
    print("=="*100)
    print(rows)
    for row in rows:
        query = "DELETE FROM public.services_clientmodel WHERE id="+str(row[0])
        print(query)
        cur.execute(query)
        print("delete success")
        conn.commit()

    print("Deleted records")
    
    return redirect('../')

def update_date_view(request):
    if request.method == 'GET':
        return render(request, 'update_date.html')
    type_of_detail = request.POST.get('type_of_detail')
    user_email = request.POST.get('user_email')
    new_date_of_deadline = request.POST.get('new_date_of_deadline')
    days_before=int(request.POST.get('new_actual_date_on_which_reminder_is_to_be_sent'))
    new_actual_date_on_which_reminder_is_to_be_sent = days_before_to_date(new_date_of_deadline,days_before)
    print("Update wil happen")
    query = "UPDATE public.services_datestorage  SET date_of_deadline ='"+str(new_date_of_deadline)+"',actual_date_on_which_reminder_is_to_be_sent ='"+str(new_actual_date_on_which_reminder_is_to_be_sent)+"' WHERE user_email = '"+ str(user_email)+"' AND type_of_detail = '"+str(type_of_detail)+"'"
    cur.execute(query)
    conn.commit()
    
    print("Update Successful")
    return redirect('../staff_dashboard')

def set_dates_view(request):
    return render(request,'set_dates.html')

def send_email_view(request):
    if request.method == 'GET':
        return render(request, 'send_email.html')

    service_name = request.POST.get('service_name')
    subject_mail = request.POST.get('subject_mail')
    email_body = request.POST.get('email_body')
    query_id = "SELECT email FROM public.services_clientmodel WHERE "+str(service_name)+"= True "
    cur.execute(query_id)
    rows = cur.fetchall()
    print("=="*100)
    print(rows)

    emails = []
    for i in rows:
        for j in i:
            emails.append(j)

    print(emails)
    send_mail(
    subject_mail,
    email_body,
    EMAIL_HOST_USER,
    emails,
    fail_silently=False,)

    print("Mail sent")
    return redirect('../')


def change_email_body_view(request):
    return render(request, 'change_email_body.html')

def update_client_view(request):
    if request.method == 'GET':
        return render(request, 'update_client.html')

    emails = request.POST.get('email')
    pan = request.POST.get('pan')

    income_tax= request.POST.get('check_01')
    gst_tax= request.POST.get('check_02')
    accounting= request.POST.get('check_03')
    companies= request.POST.get('check_04')
    other_service1= request.POST.get('check_05')
    other_service2= request.POST.get('check_06')
    other_service3= request.POST.get('check_07')
    other_service4= request.POST.get('check_08')
    
    if(str(income_tax)=='None'):
        income_tax=0
    if(str(gst_tax)=='None'):
        gst_tax=0
    if(str(companies)=='None'):
        companies=0
    if(str(accounting)=='None'):
        accounting=0
    if(str(other_service1)=='None'):
        other_service1=0
    if(str(other_service2)=='None'):
        other_service2=0
    if(str(other_service3)=='None'):
        other_service3=0
    if(str(other_service4)=='None'):
        other_service4=0

    query_id = "SELECT id FROM public.services_clientmodel WHERE email='"+str(emails)+"' and pan='"+str(pan)+"'"
    cur.execute(query_id)
    rows = cur.fetchall()
    print("=="*100)
    print(rows)
    for row in rows:
        query = "UPDATE public.services_clientmodel SET income_tax_activate='"+str(income_tax)+"',gst_tax_activate='"+str(gst_tax)+"',accounting_activate='"+str(accounting)+"',companies_activate='"+str(companies)+"',other_service1='"+str(other_service1)+"',other_service2='"+str(other_service2)+"',other_service3='"+str(other_service3)+"',other_service4='"+str(other_service4)+"' WHERE id="+str(row[0])  
        print(query)
        cur.execute(query)
        print("update success")
        conn.commit()
        
    return redirect('../')
    

def filter_clients_views(list_of_services):
    
    if request.user.is_authenticated:
        query="SELECT * FROM public.services_clientmodel WHERE ca_name='"+str(ca_name)
        ca_name=request.user.get_full_name()
        print(ca_name)
        if 'income_tax' in list_of_services:
            query = query + "and income_tax_activate"
        if 'gst_tax' in list_of_services:
            query = query + "and gst_tax_activate"
        if 'companies' in list_of_services:
            query = query + "and companies_activate"
        if 'accounting' in list_of_services:
            query = query + "and accounting_activate"
        if 'other_service1' in list_of_services:
            query = query + "and other_service1"
        if 'other_service2' in list_of_services:
            query = query + "and other_service2"
        if 'other_service3' in list_of_services:
            query = query + "and other_service3"
        if 'other_service4' in list_of_services:
            query = query + "and other_service4"
        # f_name,l_name=ca_name.split("  ")
        # ca_name=f_name+" "+l_name
        # print(ca_name)
    # query="SELECT * FROM public.services_clientmodel WHERE ca_name='"+str(ca_name)+"'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()


    list_of_services=[]
    filer_client_views(list_of_services)
    # print(rows)
    # print(type(rows))
    args={'rows':rows}
    # print(args)
    return render(request,'client_details.html',args)