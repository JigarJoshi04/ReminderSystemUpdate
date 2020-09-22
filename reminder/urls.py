"""reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from services.views import *
from authentication.views import *
from mail.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    
    # services
    # path('profile/<email>/incometax/', incometax_view, name="incometax"),
    # path('profile/<email>/gst/', gst_view, name="gst"),
    # path('profile/<email>/companies_act/', companies_act_view, name="companies_act"),
    # path('profile/<email>/accounting/', accounting_view, name="accounting"),
    
    # client profile
    # path('profile/<email>/', profile_view, name='profile'),
    
    
    # path('aboutus/', aboutus_view, name="aboutus"),
    # path('team/', team_view, name="team"),

    #authenticate
    path('ca_login/', ca_login_view, name="ca_login"),
    path('staff_login/', staff_login_view, name="staff_login"),
    path('ca_signup/', ca_signup_view, name="ca_signup"),
    path('staff_signup/', staff_signup_view, name="staff_signup"),
    path('logout/', logout_view, name="logout"),

    # # ca views
    path('ca_dashboard/', ca_dashboard_view, name="ca_dashboard"),
    path('ca_dashboard/add_client/', add_client_view, name="add_client"),
    path('ca_dashboard/client_details/', client_details_view, name="client_details"),
    path('ca_dashboard/completed_tasks/', completed_tasks_view, name="completed_tasks"),
    path('ca_dashboard/pending_tasks/', pending_tasks_view, name="pending_tasks"),
    path('ca_dashboard/failed_tasks/', failed_tasks_view, name="failed_tasks"),
    path('ca_dashboard/delete_client/', delete_client_view, name="delete_client"),
    path('ca_dashboard/update_date/', update_date_view, name="update_date"),
    path('ca_dashboard/set_dates/', set_dates_view, name="set_dates"),
    #services
    path('ca_dashboard/set_dates/gst/', gst_view, name="gst"),
    path('ca_dashboard/set_dates/incometax/', incometax_view, name="incometax"),
    path('ca_dashboard/set_dates/accounting/', accounting_view, name="accounting"),
    path('ca_dashboard/set_dates/companies_act/', companies_act_view, name="companies_act"),
    path('ca_dashboard/set_dates/', set_dates_view, name="set_dates"),
    path('ca_dashboard/set_dates/other_service1/', other_service1_view, name="other_service1"),
    path('ca_dashboard/set_dates/other_service2/', other_service2_view, name="other_service2"),
    path('ca_dashboard/set_dates/other_service3/', other_service3_view, name="other_service3"),
    path('ca_dashboard/set_dates/other_service4/', other_service4_view, name="other_service4"),
    path('ca_dashboard/send_email/', send_email_view, name="send_email"),
    path('ca_dashboard/update_client/',update_client_view, name="update_client"),
    path('ca_dashboard/change_email_body/', change_email_body_view, name="change_email_body"),
    

    # staff views
    path('staff_dashboard/', staff_dashboard_view, name="staff_dashboard"),
    path('staff_dashboard/add_client/', add_client_view, name="add_client"),
    path('staff_dashboard/update_client/', update_client_view, name="update_client"),
    # path('staff_dashboard/update_client_date/', update_client_date_view, name="update_client_date"),
    
]
