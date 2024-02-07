from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #URLS for Home Page
    path('',homepage,name='crmhome'),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('course/',course,name="course"),
    path('enroll/', enroll, name="enroll"),
    path('login/', login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    #URLS for Student Page
    path('menu/', student_interface,name='student_menu'),
    path('main_interface/', main_interface_admin,name = 'main_interface'),
    path('student/',student,name="student"),
    path('coursefun', course_search, name="coursefun"),
    path('demo_page/<int:record_id>/',move_demo_page,name="demourl"),
    path('show_demo/',show_demo,name="show_demo"),
    path('remove_student/<int:record_id>/',remove_student_data,name="remove_data"),
    path('show_remove_data/', show_removed_data, name="remove_data_url"),
    path("remove/<int:record_id>/", remove_student,name="remove_demo"),
    path('add_user/', add_user, name='add_user'),
    path('success/', success, name='success_url'),
    path('addstudent/', add_student, name='addstudent'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
