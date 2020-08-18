from django.shortcuts import render,redirect
from .models import Destination,UserList,DirectoryCreation,DirectoryMembers
from .resources import UserListResource,DirectoryResource
from django.contrib import messages
from tablib import Dataset 
from django.http import HttpResponse
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.core import mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import DirectoryCreationForm
def index(response):
    dests=DirectoryCreation.objects.all()
    return render(response, "socius/index.html",{'dests':dests})

def about(request):
    return render(request, "socius/about.html")
@login_required
def simple_upload(request):
    if request.method == 'POST':
        user_list = UserListResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'socius/upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        #print(imported_data)
        d=[]
        for data in imported_data:
            d.append(data[2])
            value = UserList(
        		data[0],
        		data[1],
        		data[2],
        		)
            value.save()
        l=d
        user=User.objects.filter(is_superuser='True').first()
        current_site = get_current_site(request)
        mail_subject = 'Invite to Socius'
        message = render_to_string('accounts/invite.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        for i in l:
            #reciever_list.append(i['email'])
            to_email = i
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Invitations sended')
                
    return render(request, 'socius/upload.html')
def active(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
      #  user.save()
        if user.is_active==True:
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            return redirect('register')
    else:
        return HttpResponse('Invitation link is invalid!')
@login_required
def create(request,*args,**kwargs):
    if request.method=='POST':
        form=DirectoryCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=DirectoryCreationForm()
    return render(request,'socius/createdir.html',{'form':form})
   
    #return render(request,'socius/createdir.html')
def created(request):
    return redirect('index')

    
   
def about(request):
   return render(request,'socius/about.html')
@login_required
def joindirectory(request):
    return render(request,'socius/joindirectory.html')

def joined(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['email']
        Bio=request.POST['bio']
        if DirectoryMembers.objects.filter(Email=Email).exists():
            messages.info(request, 'The email is already registered')
            return redirect('joined')
        else:
            obj2=DirectoryMembers(Name=Name,Email=Email,Bio=Bio)
            obj2.save()
            direcory1=DirectoryCreation.objects.all()
            return render(request,'socius/directorypage.html')
    else:
        return render(request,'socius/joindirectory.html')

def members(response):
   Members=DirectoryMembers.objects.all()
   return render(response, "socius/Members.html",{'Members':Members})

def viewdirectory(request):
    admin=User.objects.filter(is_superuser='True').first()
    return render(request,'socius/directorypage.html',{'admin':admin})
