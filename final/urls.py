from django.urls import path
from accounts import views
from django.contrib import admin
from socius import views as v
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('admin', admin.site.urls),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('index', views.login, name="index"),
    path('logout', views.logout, name="logout"),
    path('about', v.about, name="about"),
    path('upload',v.simple_upload,name="upload"),
    path('create',v.create,name="create"),
    path('created',v.created,name="created"),
    path('joined',v.joined,name="joined"),
    path('members',v.members,name="members"),
    path('viewdirectory',v.viewdirectory,name="viewdirectory"),
    path('joindirectory',v.joindirectory,name="joindirectory"),
    path('', v.index, name="index"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('active/<uidb64>/<token>/',v.active, name='active'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
    
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''

