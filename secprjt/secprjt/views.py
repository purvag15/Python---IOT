import pymysql as ps
from django.shortcuts import render
import datetime
import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
def student(request):
    return render(request,'customer.html')

def customer(request):
    conn=ps.connect(host='localhost',port=3307,user='root',password='123',db='Bank')
    cmd=conn.cursor()
    am = request.POST['ab']
    fn = request.POST['ac']
    ln = request.POST['ad']
    do = request.POST['ae']
    gn = request.POST['aa']
    mn = request.POST['al']
    em = request.POST['ak']
    ad = request.POST['af']
    vd = request.POST['ag']
    st = request.POST['ah']
    pw = request.POST['am']
    pi = request.POST['an']
    pic=request.FILES['pic']
    q="insert into Customer values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(am,fn,ln,do,gn,mn,em,ad,vd,st,pw,pi,pic.name)
    cmd.execute(q)
    conn.commit()
    f=open('e:/secprjt/asset/'+pic.name,'wb')
    for bytes in pic.chunks():
        f.write(bytes)
    f.close()    

    conn.close()
    return render(request,'thankyou.html')

def login_view(request):
    return render(request,'login.html',{'msg':''})

def check_pin(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    pin=request.GET['pin']
    K = datetime.datetime.now()
    q = "select * from Customer where email='{}' and password='{}'".format(request.session['SES_CUST'][6], pin)
    cmd.execute(q)
    row=cmd.fetchone()
    
    if(row==None):
        status='Invalid'
    else:
        status="Valid"
    print(status)
    if(status=='Valid'):
        q = "select * from employeecustomer where customerid='{}' and status='Allow' and date='{}'".format(request.session['SES_CUST'][6], K.strftime('%d-%B-%Y'))
        cmd.execute(q)
        row=cmd.fetchone()
        if(row==None):
         status='Close'
        else:
         status="Open"
    print(status)     
    connectWithIOT(status)
    conn.close()      

    return render(request,'notepad.html')

def show_keypad(request):
    try:
        row=request.session['SES_CUST']
        return render(request,'notepad.html')
    except:
        return render(request,'login.html')

def login(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    login = request.GET['login']
    pwd = request.GET['pwd']
    q="select * from Customer where email='{}' and password='{}'".format(login,pwd)
    cmd.execute(q)
    row=cmd.fetchone()
    conn.close()
    if(row==None):
        return render(request,'login.html',{'msg':'Invalid Id/Password'})
    else:
        request.session['SES_CUST']=row
        K=datetime.datetime.now()
        request.session['SES_LOGINTIME']=K.strftime('%A %d-%B-%Y %H:%M:%S')
        return render(request,'customerhome.html')
def view1(request):
    return render(request,'adminlogin.html',{'msg2':''})

def admin(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    l = request.GET['al']
    w = request.GET['apwd']
    q="select * from admins where adminemail='{}' and adminpassword='{}'".format(l,w)
    cmd.execute(q)
    x=cmd.fetchone()
    conn.close()
    if(x==None):
        return render(request,'adminlogin.html',{'msg2':'INVALID CREDENTIALS'})
    else:
        return render(request,'adminhome.html')

def employee_view(request):
    return render(request,'employee.html')

def employee(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    am = request.GET['ei']
    fn = request.GET['en']
    ln = request.GET['dob1']
    do = request.GET['gen']
    gn = request.GET['des']
    mn = request.GET['email1']
    em = request.GET['mob1']
    ad = request.GET['add']
    vd = request.GET['city']
    st = request.GET['state']
    pw = request.GET['pwd1']
    q  = "insert into Employee values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(am,fn,ln,do,gn,mn,em,ad,vd,st,pw)
    cmd.execute(q)
    conn.commit()
    conn.close()
    return render(request, 'thankyou.html')

def employee_login(request):
    return render(request, 'employeelogin.html',{'msg1':''})

def elogin(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    alogin = request.GET['el']
    apwd = request.GET['epwd']
    q = "select * from Employee where Email='{}' and Password='{}'".format(alogin, apwd)
    cmd.execute(q)
    row1 = cmd.fetchone()
    conn.close()
    if (row1==None):
        return render(request,'employeelogin.html',{'msg1':'INVALID CREDENTIALS'})
    else:
        request.session['SES_EMP'] = row1
        K = datetime.datetime.now()
        request.session['SES_LOGINTIME'] = K.strftime('%A %d-%B-%Y %H:%M:%S')
        return render(request,'employeehome.html',{'fn':'SEE HERE','ln':'SEE HERE','dob':'SEE HERE','gen':'SEE HERE','mob':'SEE HERE','em':'SEE HERE','ad':'SEE HERE','vd':'SEE HERE','st':'SEE HERE','pwd':'SEE HERE','pin':'SEE HERE'})
def employee_home(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    acc=request.GET['acc']
    q="select * from Customer where accno='{}'".format(acc)
    cmd.execute(q)
    row2=cmd.fetchone()
    conn.close()
    if(row2==None):
        return render(request,'employeehome.html',{'fn':'DO NOT EXIST','ln':'DO NOT EXIST','dob':'DO NOT EXIST','gen':'DO NOT EXIST','mob':'DO NOT EXIST','em':'DO NOT EXIST','ad':'DO NOT EXIST','vd':'DO NOT EXIST','st':'DO NOT EXIST','pwd':'DO NOT EXIST','pin':'DO NOT EXIST'})
    else:
        return render(request,'employeehome.html',{'fn':row2[1],'ln':row2[2],'dob':row2[3],'gen':row2[4],'mob':row2[5],'em':row2[6],'ad':row2[7],'vd':row2[8],'st':row2[9],'pwd':row2[10],'pin':row2[11]})

def change_password(request):
   return render(request,'changepwd.html',{'qmsg':''})
def change_pwd(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    cupwd=request.GET['pwd1']
    pw=request.GET['pwd2']
    pw1=request.GET['pwd3']
    if(pw==pw1):
       w="select * from Customer where email='{}' and password='{}'".format(request.session['SES_CUST'][6],cupwd)
       cmd.execute(w)
       row2=cmd.fetchone()

       if(row2 is not None):
        q1="update Customer set password='{}' where accno='{}'".format(pw,request.session['SES_CUST'][0])
        cmd.execute(q1)
        print('yt')
        conn.commit()
        return render(request,'changepwd.html',{'qmsg':'Succesfully Changed'})
       else:
        return render(request, 'changepwd.html', {'qmsg': 'CHECK CURRENT PASSWORD'})

       conn.close()

    else:
        return render(request, 'changepwd.html', {'qmsg': 'CONFIRM PASSWORD NOT MATCHED'})
def change_pin(request):
   return render(request,'changepin.html',{'rmsg':''})
def change_PIN(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    cupwd = request.GET['pin1']
    pw = request.GET['pin2']
    pw1 = request.GET['pin3']
    if (pw == pw1):
        w = "select * from Customer where email='{}' and pin='{}'".format(request.session['SES_CUST'][6], cupwd)
        cmd.execute(w)
        row2 = cmd.fetchone()
        if (row2 is not None):
            q1 = "update Customer set pin='{}' where accno='{}'".format(pw, request.session['SES_CUST'][0])
            cmd.execute(q1)
            print('yt')
            conn.commit()
            return render(request, 'changepin.html', {'rmsg': 'Succesfully Changed'})
        else:
            return render(request, 'changepin.html', {'rmsg': 'CHECK CURRENT PASSWORD'})

        conn.close()

    else:
        return render(request, 'changepin.html', {'rmsg': 'CONFIRM PASSWORD NOT MATCHED'})

def cust_logout(request):
    del request.session['SES_CUST']
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def employee_customer(request):
    conn = ps.connect(host='localhost', port=3307, user='root', password='123', db='Bank')
    cmd = conn.cursor()
    
    K = datetime.datetime.now()
    request.session['SES_TIME'] = K.strftime('%H:%M:%S')
    request.session['SES_DATE'] = K.strftime('%d-%B-%Y')
    a=request.GET['cust_email']
    b=request.session['SES_EMP'][0]
    c=request.session['SES_DATE']
    d=request.session['SES_TIME']
    e=request.GET['status']
    q="insert into employeecustomer(customerid,employeeid,date,time,status) values ('{}','{}','{}','{}','{}')".format(a,b,c,d,e)
    cmd.execute(q)
    conn.commit()
    conn.close()
    return render(request, 'employeehome.html', {'fn': 'SEE HERE', 'ln': 'SEE HERE', 'dob': 'SEE HERE', 'gen': 'SEE HERE', 'mob': 'SEE HERE', 'em': 'SEE HERE', 'ad': 'SEE HERE', 'vd': 'SEE HERE', 'st': 'SEE HERE', 'pwd': 'SEE HERE','pin': 'SEE HERE','jop':'Done Succesfully'})



def connectWithIOT(value):
 pc=PNConfiguration()
 pc.subscribe_key="sub-c-88748fa0-9c8c-11e9-ab0f-d62d90a110cf"
 pc.publish_key="pub-c-9687c108-59d1-4d77-a4f7-289f64564b77"
 pc.ssl=True
 pubnub = PubNub(pc)
 # Listen for Messages on the Market Order Channel
 channel = 'lock'
 pubnub.publish().channel(channel).message(value).pn_async(show)
 time.sleep(2)

def show(msg,stat):
    if(msg and stat):print(msg.timetoken,stat.status_code)
    else:
        print("Error",stat and stat.status_code)    

    




