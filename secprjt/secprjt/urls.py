"""secprjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
        path('admin/', admin.site.urls),
        path("customer_view/",views.student),
        path("customer",views.customer),
        path("login_view/",views.login_view),
        path("login/",views.login),
        path("admin_login/",views.admin),
        path("admin_view/",views.view1),
        path("employee_view/",views.employee_view),
        path("employee/",views.employee),
        path("employee_loginview/", views.employee_login),
        path("employee_login/",views.elogin),
        path("keypad/",views.show_keypad),
        path("check_pin",views.check_pin),
        path("employee_home",views.employee_home),
        path("change_password",views.change_password),
        path("change_pwd",views.change_pwd),
        path("change_pin",views.change_pin),
        path("change_PIN",views.change_PIN),
        path("cust_logout/",views.cust_logout),
        path("home/",views.index),
	path("employee_customer/",views.employee_customer),

]
urlpatterns+=staticfiles_urlpatterns()