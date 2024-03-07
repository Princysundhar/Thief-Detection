import datetime
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
import random
# Create your views here.

def log(request):
    return render(request,"index.html")

def log_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"

        if data.type =='admin':
            return redirect('/admin_home')
        else:
            return redirect('/police_home')
    else:
        return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")


def admin_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")

    return render(request,"admin/index.html")

def police_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")

    return render(request,"policestation/index.html")

# Police station management

def police_add(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        return render(request,"admin/add_police.html")

def police_add_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']

        res = random.randint(0000,9999)


        lob = login.objects.filter(username=email)
        if lob.exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/worker_register'</script>")
        else:
            log_obj = login()
            log_obj.username = email
            log_obj.password = res
            log_obj.type = 'policestation'
            log_obj.save()

            obj = police_station()
            obj.name = name
            obj.place = place
            obj.post = post
            obj.pin = pin
            obj.email = email
            obj.contact = contact
            obj.LOGIN = log_obj
            obj.save()
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Police Adding..")
            msg['Subject'] = 'Verification'
            msg['To'] = email
            msg['From'] = 'riss.princytv@gmail.com'
            try:
                gmail.send_message(msg)
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))

            return HttpResponse("<script>alert('Success');window.location='/view_police'</script>")

def view_police(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = police_station.objects.all()
        return render(request,"admin/view_police.html",{"data":data})

def update_police(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = police_station.objects.get(id=id)
        return render(request,"admin/update_police.html",{"data":data})

def update_police_post(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']
        police_station.objects.filter(id=id).update(name = name,place=place,post=post,pin=pin,email=email,contact=contact)
        return HttpResponse("<script>alert('Updated');window.location='/view_police#kk'</script>")

def delete_police(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = police_station.objects.get(LOGIN = id).delete()

        # print(data)
        return HttpResponse("<script>alert('Deleted');window.location='/view_police#kk'</script>")

# Crminal category Management

def add_criminal_category(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        return render(request,"admin/add_category.html")

def add_criminal_category_post(request):
    data = crime_category.objects.all()
    if data.exists():
        return HttpResponse("<script>alert('Add another crime');window.location='/add_criminal_category'</script>")
    else:

        category = request.POST['textfield']
        obj = crime_category()
        obj.category_name = category
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/add_criminal_category'</script>")

def view_category(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = crime_category.objects.all()
        return render(request,"admin/view_category.html",{"data":data})

def delete_category(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        crime_category.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_category'</script>")

def view_detection_details(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = alert.objects.all()
        return render(request,"admin/view_detection_details.html",{"data":data})

def view_criminals(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = criminals.objects.all()
        return render(request,"admin/view_criminals.html",{"data":data})

def view_user(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = user.objects.all()
        return render(request,"admin/view_user.html",{"data":data})

def logout(request):
    request.session['lg']=" "
    return redirect('/')


###########################################################################################

# police station module

def view_profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = police_station.objects.get(LOGIN=request.session['lid'])
        # print(data)
        return render(request,"policestation/view_profile.html",{"data":data})

# criminal Management

def add_criminal(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = crime_category.objects.all()
        return render(request,"policestation/add_criminal.html",{"data":data})

def add_criminal_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        category = request.POST['select']
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        ID_proof = request.FILES['fileField']
        photo = request.FILES['fileField2']

        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\Thief_Detection\Thief\static\photo\\" + dt + '.jpg', photo)
        fs.save(r"C:\Users\DELL\PycharmProjects\Thief_Detection\Thief\static\ID proof\\" + dt + '.pdf', ID_proof)
        photo = '/static/photo/' + dt + '.jpg'
        ID_proof = '/static/ID proof/'+dt+'.pdf'

        obj = criminals()
        obj.CATEGORY = crime_category.objects.get(id=category)
        obj.POLICE = police_station.objects.get(LOGIN=request.session['lid'])
        obj.name = name
        obj.gender = gender
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.contact = contact
        obj.photo = photo
        obj.id_proof = ID_proof
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/add_criminal'</script>")

def view_criminal(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = criminals.objects.all()
        return render(request,"policestation/view_criminal.html",{"data":data})

def update_criminal(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        data = criminals.objects.get(id=id)
        data1 = crime_category.objects.all()
        return render(request,"policestation/update_criminal.html",{"data":data,"data1":data1})

def update_criminal_post(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        category = request.POST['select']
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        ID_proof = request.FILES['fileField']
        photo = request.FILES['fileField2']
        criminals.objects.filter(id=id).update(category=category,name=name,gender=gender,
                                               age=age,place=place,post=post,pin=pin,contact=contact,id_proof=ID_proof,photo=photo)
        return HttpResponse("<script>alert('Updated');window.location='/view_criminal#kk'</script>")

def delete_criminal(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:
        criminals.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_criminal#kk'</script>")


def view_users(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:

        data = user.objects.all()
        return render(request,"policestation/view_user.html",{"data":data})

def view_crminal_alert(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/log'</script>")
    else:

        data = alert.objects.filter(CRIMINALS__POLICE=request.session['lid'])
        return render(request, "policestation/view_criminal_alert.html",{"data":data})

######################################################################################################

# User module(android)

def android_login(request):
    username = request.POST['name']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        logininstance = login.objects.get(id=lid)
        res = user.objects.get(LOGIN=logininstance)
        type = data[0].type
        name = res.name
        email = res.email
        photo = res.photo
        # print(photo)
        return JsonResponse({"status":"ok",'type':type,'lid':lid,'name':name,'email':email,'photo':photo})
    else:
        return JsonResponse({"status":None})


def android_user_registration(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    photo = request.FILES['pic']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Thief_Detection\Thief\static\photo\\"+d+'.jpg',photo)
    photo = '/static/photo/'+d +'.jpg'
    data = login.objects.filter(username=email)
    if data.exists():
        return  JsonResponse({"status":None})
    else:

        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'user'
        log_obj.save()

        obj = user()
        obj.name = name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.photo = photo
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({"status":"ok"})

def android_view_profile(request):
    vid = request.POST['lid']
    res = user.objects.get(LOGIN=vid)
    return JsonResponse({"status":"ok","name":res.name,"place":res.place,
                         "post":res.post,"pin":res.pin,"email":res.email,"contact":res.contact,"photo":res.photo})

def android_view_visitorlog(request):
    lid = request.POST['lid']
    res = visitor_log.objects.filter(CAMERA__USER__LOGIN=login.objects.get(id=lid))
    ar = []
    for i in res:
        ar.append(
            {
                "vid":i.id,
                "image":i.image,
                "date":i.date,
                "time":i.time,
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_femiliarlog(request):
    lid = request.POST['lid']
    res = familiar_log.objects.filter(FAMILIAR_PERSON__USER__LOGIN=lid)
    # res = familiar_person.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "fid":i.id,
                "fname":i.FAMILIAR_PERSON.F_name,
                "fcontact":i.FAMILIAR_PERSON.F_contact,
                "fimage":i.FAMILIAR_PERSON.F_image,
                "date":i.date,
                "time":i.time
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_criminal(request):
    res = criminals.objects.all()
    ar =[]
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "name":i.name,
                "category":i.CATEGORY.category_name,
                "age":i.age,
                "gender":i.gender,
                "place":i.place,
                "post":i.post,
                "pin":i.pin,
                "id_proof":i.id_proof,
                "contact":i.contact,
                "photo":i.photo
            }
        )
    return JsonResponse({"status":"ok","data":ar})

#### Femiliar person Management

def android_add_familiar_person(request):
    lid = request.POST['lid']
    name = request.POST['name']
    place = request.POST['place']
    email = request.POST['email']
    contact = request.POST['contact']
    photo = request.FILES['pic']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Thief_Detection\Thief\static\photo\\" + d + '.jpg', photo)
    photo = '/static/photo/' + d + '.jpg'
    obj = familiar_person()
    obj.F_name = name
    obj.F_place = place
    obj.F_email = email
    obj.F_contact = contact
    obj.F_image = photo
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_familiar_person(request):
    lid = request.POST['lid']
    fid = request.POST['fid']
    res = familiar_person.objects.filter(USER__LOGIN=lid)
    ar =[]
    for i in res:
        ar.append(
            {
                "fid":i.id,
                "fname":i.F_name,
                "fplace":i.F_place,
                "femail":i.F_email,
                "fcontact":i.F_contact,
                "fimage":i.F_image
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_delete_familiar_person(request):
    fid = request.POST['fid']
    print(fid)
    familiar_person.objects.get(id=fid).delete()
    return JsonResponse({"status":"ok"})



def android_update_familiar_persons(request):
    fid = request.POST['fid']
    res = familiar_person.objects.get(id=fid)
    return JsonResponse({"status": "ok", "name": res.F_name, "place": res.F_place,
                         "email": res.F_email, "contact": res.F_contact,"photo":res.F_image})

def android_update_familiar_person(request):

    try:
        fid = request.POST['fid']
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        photo = request.FILES['pic']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\Thief_Detection\Thief\static\photo\\" + d + ".jpg", photo)
        path = '/static/photo/' + d + ".jpg"
        familiar_person.objects.filter(id=fid).update(F_name=name,F_place =place,F_email=email,F_contact=contact,F_image=path)
        return JsonResponse({"status":"ok"})

    except Exception as e:

        fid = request.POST['fid']
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        familiar_person.objects.filter(id=fid).update(F_name=name, F_place=place, F_email=email, F_contact=contact)
        return JsonResponse({"status": "ok"})

















####### camera management##########

def android_add_camera(request):
    camera_no = request.POST['camera_no']
    obj = camera()
    obj.camera_number = camera_no
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_camera(request):

    res = camera.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "camera_no":i.camera_number
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_delete_camera(request):
    cid = request.POST['cid']
    camera.objects.filter(id=cid).delete()
    return JsonResponse({"status":"ok"})










