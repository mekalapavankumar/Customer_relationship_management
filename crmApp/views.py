from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth import authenticate,login
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


# homepage view
def homepage(request):
    # return HttpResponse('crm app has called')
    obj = NewStudentForm()
    if request.method == "POST":
        cobj = NewStudentForm(request.POST)
        if cobj.is_valid() == True:
            cobj.save()
            return HttpResponse("Data is Saved Successfully")
        else:
            cobj = obj
            return render(request, 'homepage.html')
    return render(request, 'homepage.html', {'data': obj})


def about(request):
    obj = NewStudentForm()
    if request.method == "POST":
        cobj = NewStudentForm(request.POST)
        if cobj.is_valid() == True:
            cobj.save()
            return HttpResponse("Data is Saved Successfully")
        else:
            cobj = obj
        return redirect('crmhome')
    return render(request, 'about.html', {'data': obj})


def contact(request):
    return render(request, 'contact.html')

# course functionalities
def course(request):
    return render(request, 'course.html')

def main_interface_admin(request):
    return render(request,'admin/main_interface.html')

# Admin Page view
@login_required(login_url='login')
def student(request):
    obj = NewStudent.objects.all()
    st = {'st':obj}
    return render(request, 'Admin/student_data.html', st)

# display the course data department wise
def course_search(request):
    cobj = {}
    if request.method == 'POST':
        co = request.POST['word']
        product = NewStudent.objects.filter(course__icontains=co)
        cobj['product'] = product
        return render(request, 'Admin/search.html', cobj)
    return render(request, 'Admin/search.html')


# move student data to demo page view
def move_demo_page(request, record_id):
    demo_move_page = NewStudent.objects.get(id=record_id)
    move_to = Student_Demo.objects.create(Name=demo_move_page.Name,email=demo_move_page.email,Mobile=demo_move_page.Mobile,gender=demo_move_page.gender,course=demo_move_page.course)
    demo_move_page.delete()
    return redirect('student')


def show_demo(request):
    obj = Student_Demo.objects.all()
    return render(request, 'Admin/demo_page.html', {'form': obj})


def remove_student_data(request, record_id):
    demo_move_page = NewStudent.objects.get(id=record_id)
    move_to = Remove_student.objects.create(Name=demo_move_page.Name,email=demo_move_page.email,Mobile=demo_move_page.Mobile,gender=demo_move_page.gender,course=demo_move_page.course)
    demo_move_page.delete()
    return redirect('student')


def show_removed_data(request):
    obj = Remove_student.objects.all()
    return render(request, 'Admin/remove_data.html', {'form': obj})


def remove_student(request, record_id):
    demo_move_page = Student_Demo.objects.get(id=record_id)
    move_to = Remove_student.objects.create(Name=demo_move_page.Name,email=demo_move_page.email,Mobile=demo_move_page.Mobile,gender=demo_move_page.gender,course=demo_move_page.course)
    demo_move_page.delete()
    return redirect('remove_data_url')


def add_user(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        demo = Student_Demo.objects.get(id=record_id)
        username = demo.Name.lower().replace(" ", "")
        password = User.objects.make_random_password()

        # Send the username, password, and message to the user via email
        message = f'Thank you for Registering into VCube Software Solutions Pvt.Ltd.\n\n'
        message += f'Username: {username}\nPassword: {password}\n\n'
        message += f'Please keep your Credentials Confidential and change your password for security purposes.'

        send_mail(
            'Your Account Details',
            message,
            'pvnkumar.mekala@gmail.com',
            [demo.email],
            fail_silently=False
        )

        user = get_user_model().objects.create(
            username=username,
            password=make_password(password),
            email=demo.email
        )

        demo.user = user
        demo.save()
        #return HttpResponse('Mail sent')
        #messages.success(request,'Data Added Successfully')
        return redirect('success_url')

    return HttpResponseNotAllowed(['POST'])


def success(request):
    return render(request, 'admin/success.html')


objects = models.Manager()
def add_student(request):
    std_info=StudentForm
    course1 = NewStudent.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            #form = StudentForm()
            return HttpResponse('cannot access the account')

    return render(request, 'admin/add_student.html', {'form': std_info,'course':course1})

# Enroll view
def enroll(request):
    context = {}
    cform = NewStudentForm()
    context['form'] = cform
    if request.method == "POST":
        obj = NewStudentForm(request.POST)
        if obj.is_valid() == True:
            obj.save()
            return HttpResponse('Your account is created')
        else:
            context['form'] = obj
            return HttpResponse('404 - not Found')
    return render(request, 'enroll.html', context)


# login  view
def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        valid_user = authenticate(request, username=uname, password=pwd)
        if valid_user is not None:
            login(request, valid_user)
            # return redirect('displayurl')
            return redirect('student_menu')
        else:
            messages.success(request,"Invalid Credentials, Please Try Again!")
    return render(request, 'login.html')


# logout functionalities
def logout_view(request):
    logout(request)
    return redirect('login')

#Student Menu Interface for admin
def student_interface(request):
    return render(request,'admin/menu_interface.html')
