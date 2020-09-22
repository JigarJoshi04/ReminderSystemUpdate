from django.shortcuts import render
import psycopg2
from background_task import background
import datetime as dt
from reminder.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from datetime import datetime,timedelta,date
import calendar
from dateutil.relativedelta import relativedelta
from mail.models import *

# Create your views here.
current_date = '2020-08-06'
conn = psycopg2.connect(database="reminder_website", user = "postgres", password = "jigarpinakin", host = "localhost", port = "5432")
cur = conn.cursor()
main_message = ""

def update_service_date(date_today):
    query = "SELECT service_type,date_of_deadline,recurrence_type,actual_date_on_which_reminder_is_to_be_sent,service_name FROM public.services_servicedatemodel WHERE actual_date_on_which_reminder_is_to_be_sent ='"+str(date_today)+"'"
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)

    for i in range(len(rows)):
        new_date_of_deadline = rows[i][1] + relativedelta(months=+int(rows[i][2]))
        print(new_date_of_deadline)
        new_reminder_date = rows[i][3] + relativedelta(months=+int(rows[i][2]))
        print(new_reminder_date)
        print("WE THE BEST"*100)
        print(new_date_of_deadline.strftime("%x"))
        print(new_reminder_date.strftime("%x"))
        query = "UPDATE public.services_servicedatemodel  SET date_of_deadline ='"+str(new_date_of_deadline)+"',actual_date_on_which_reminder_is_to_be_sent ='"+str(new_reminder_date)+"' WHERE service_type ='"+str(rows[i][0])+"'"
        cur.execute(query) 
        conn.commit()
        print(rows)

        #Insert the updated date in schedule task
        obj = ScheduleTaskModel(service_name=rows[i][4],service_type=rows[i][0],date_of_deadline=new_date_of_deadline,actual_date_on_which_reminder_is_to_be_sent=new_reminder_date,recurrence_type=rows[i][2],email_data='Hi reminder')
        obj.save()

def service_name_change(serv):
    if serv == 'Income Tax':
        return 'income_tax_activate'
    elif serv == 'GST':
        return 'gst_tax_activate'
    elif serv == 'Accounting Act':
        return 'accounting_activate'
    elif serv == 'Companies Act':
        return 'companies_activate'        
    else:
        return 'other_service'+str(serv)[-1] 


@background()
def email_sender(date_today):
    query = "SELECT service_name,service_type,email_data FROM public.mail_scheduletaskmodel WHERE actual_date_on_which_reminder_is_to_be_sent ='"+str(date_today)+"'"
    cur.execute(query)
    rows = cur.fetchall()
    for i in range(len(rows)):
        serv = service_name_change(str(rows[i][0]))
         
        query = "SELECT email,client_name,client_type,pan FROM public.services_clientmodel WHERE "+str(serv)+" = True "
        cur.execute(query)
        rows1 = cur.fetchall()
        print(rows1)
        for j in range(len(rows1)):
            data = 'hiiiiii bye'
            subject_mail =  str(rows[i][1]) +' Reminder'
            send_mail(
            subject_mail,
            data,
            EMAIL_HOST_USER,
            [rows1[j][0]],
            fail_silently=False,)
            print('email senttttttttttttttttttttttttt')
            #insert
            # obj = CompletedMailModel(client_name=rows1[j][1],service_type=rows[i][0],date_of_deadline=date_of_deadline,actual_date_on_which_reminder_is_to_be_sent = reminder_before,recurrence_type = recurrence_type,email_data=email_data)
            # obj.save()

        query = "DELETE FROM public.mail_scheduletaskmodel WHERE actual_date_on_which_reminder_is_to_be_sent ='"+str(date_today)+"'"
        print(query)
        cur.execute(query)
        print("delete success")
        conn.commit()            

    


def home_view(request):
    get_date =  datetime.now()
    real_current_date = str(get_date)
    real_current_date_string = real_current_date[:10]
    print(real_current_date_string)
    global current_date
    if(real_current_date_string!=current_date):
        print("WE are scheduling")

        # Update date service date
        update_service_date(real_current_date_string)

        #mail send.
        email_sender(real_current_date_string)


        # email_ids = mail_extractor()
        # print(email_ids)
        # for i in range(0,len(email_ids)):
        #     print("for loop is inside")
        #     ca_name = get_ca_name(email_ids[i][0])
        # current_date = real_current_date_string
    return render(request, 'home.html')








# def mail_extractor():
#     print("Mails are extracting")
    # query = "SELECT user_email,type_of_detail,date_of_deadline ,id,recurrence_type FROM public.services_datestorage WHERE actual_date_on_which_reminder_is_to_be_sent ='"+str(current_date)+"'"
    # cur.execute(query)
    # rows = cur.fetchall()
    
#     print("=======================================================================================================================================")
#     print(rows)
#     print(len(rows))
#     return rows
   

# @background()
# def send_mailssss(client_type,username,email_id,service_type,date_of_deadline,ca_name):
#     print("Inside the sent amils function$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     print(email_id)
#     print(service_type)
#     print(date_of_deadline)
#     subject="You have a Request Due for "+ service_type+" Please pay the dues on or before "+ str(date_of_deadline)
    
#     if(client_type =="Person"):
#         message = "Dear "+ str(username)+' , We request you to check with your deadlines of your requests of '+str(service_type)+ 'Please pay the dues on or before the date of deadline : '+ str(date_of_deadline)+ "This ia a gentrle reminder from your CA : "+ str(ca_name) +str(main_message)
    
#     else:
#         message = "M/S "+  str(username)+' , We request you to check with your deadlines of your requests of '+str(service_type)+ 'Please pay the dues on or before the date of deadline : '+ str(date_of_deadline)+ "This ia a gentrle reminder from your CA : "+ str(ca_name) +str(main_message)
    
#     print(subject)
#     print(message)
#     reciepent = email_id
#     send_mail(subject,message,EMAIL_HOST_USER,[reciepent],fail_silently=False,)
#     print("mail is sent")

# def get_ca_name(client_email):
#     query = "SELECT ca_name FROM public.services_clientmodel WHERE email = '"+str(client_email)+"' "
#     cur.execute(query)
#     rows =cur.fetchall()
#     # print("********=====================***********************************************************************************")
#     # print(rows)
#     if(len(rows[0])!=0):
#         return rows[0][0]




# def home_view(request):
#     date_3_days_ago =  datetime.now()
#     real_current_date = str(date_3_days_ago)
#     real_current_date_string = real_current_date[:10]
#     print(real_current_date_string)
#     global current_date
#     if(real_current_date_string!=current_date):
#         print("WE are scheduling")
#         email_ids = mail_extractor()
#         print(email_ids)
#         for i in range(0,len(email_ids)):
#             print("for loop is inside")
#             ca_name = get_ca_name(email_ids[i][0])


#             ####################################################################
    
#             query_username = "SELECT client_name,client_type FROM public.services_clientmodel WHERE email = '"+str(email_ids[i][0]) +"'"
#             cur.execute(query_username)
#             rows_username = cur.fetchall()

#             ####################################################################
#             send_mailssss(client_type = rows_username[1],username = rows_username[0],ca_name = ca_name, service_type =email_ids[i][1],email_id =email_ids[i][0],date_of_deadline = str(email_ids[i][2]),verbose_name= [email_ids[i][0],real_current_date_string,ca_name])
#             print("mails_arE_sending")
            
#             #################################################################################
#             start_date = email_ids[i][2]
#             new_date_of_deadline = start_date+ relativedelta(months=+int(email_ids[i][4]))
#             print(new_date_of_deadline)
            
#             start_date = datetime.now()
        #     new_actual_date_on_which_reminder_is_to_be_sent = start_date+ relativedelta(months=+int(email_ids[i][4]))
        #     print(new_actual_date_on_which_reminder_is_to_be_sent)
        #     print("WE THE BEST"*100)
        #     print(new_date_of_deadline.strftime("%x"))
        #     print(new_actual_date_on_which_reminder_is_to_be_sent.strftime("%x"))
        #     query = "UPDATE public.services_datestorage  SET date_of_deadline ='"+str(new_date_of_deadline)+"',actual_date_on_which_reminder_is_to_be_sent ='"+str(new_actual_date_on_which_reminder_is_to_be_sent)+"' WHERE user_email = '"+ str(email_ids[i][0])+"' AND type_of_detail = '"+str(email_ids[i][1])+"' RETURNING *"
        #     print(query)
        #     cur.execute(query) 
        #     conn.commit()
        #     rows_v =cur.fetchall()
        #     print(rows_v)
        # current_date = real_current_date_string
#         print("We have scheduled")
#     return render(request, 'home.html')

def completed_tasks_view(request):
    if request.user.is_authenticated:
        ca_name=request.user.get_full_name()
        print(ca_name)
        # f_name,l_name=ca_name.split("  ")
        # ca_name=f_name+" "+l_name
        # print(ca_name)
    query="SELECT task_params FROM public.background_task_completedtask"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()

    print(rows)
    print(type(rows))
    for j in range(0,len(rows)):
        rows[j] = list(rows[j])
        for i in range(0,len(rows[j])):
            rows[j][i]=rows[j][i].replace("[","")
            rows[j][i]=rows[j][i].replace("]","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].split(",")
        
    print(rows)
    print(type(rows))

    args={'rows':rows}
    print(args)
    return render(request,'completed_tasks.html',args)

def pending_tasks_view(request):
    if request.user.is_authenticated:
        ca_name=request.user.get_full_name()
        print(ca_name)
        # f_name,l_name=ca_name.split("  ")
        # ca_name=f_name+" "+l_name
        # print(ca_name)
    query="SELECT verbose_name FROM public.background_task"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()

    print(rows)
    print(type(rows))
    for j in range(0,len(rows)):
        rows[j] = list(rows[j])
        for i in range(0,len(rows[j])):
            rows[j][i]=rows[j][i].replace("[","")
            rows[j][i]=rows[j][i].replace("]","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].split(",")
        
    print(rows)
    print(type(rows))

    args={'rows':rows}
    print(args)
    return render(request,'pending_tasks.html',args)

def failed_tasks_view(request):
    if request.user.is_authenticated:
        ca_name=request.user.get_full_name()
        print(ca_name)
        # f_name,l_name=ca_name.split("  ")
        # ca_name=f_name+" "+l_name
        # print(ca_name)
    query="SELECT verbose_name FROM public.background_task_completedtask WHERE failed_at IS NOT NULL"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    
    print(rows)
    print(type(rows))
    for j in range(0,len(rows)):
        rows[j] = list(rows[j])
        for i in range(0,len(rows[j])):
            rows[j][i]=rows[j][i].replace("[","")
            rows[j][i]=rows[j][i].replace("]","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].replace("'","")
            rows[j][i]=rows[j][i].split(",")
        
    print(rows)
    print(type(rows))

    args={'rows':rows}
    print(args)
    return render(request,'failed_tasks.html',args)