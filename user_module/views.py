from django.shortcuts import render,redirect,reverse
from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .forms import profile_form, project_form, skill_form , user_bookmark_form
from .models import project_model, profile_model, skill_model, user_bookmark_model

app_name ='user_module'

def projects(request,*args, **kwargs):  
    user_log = request.user
    if user_log.is_authenticated:
        form = project_form()
        public_obj = project_model.objects.all().exclude(user=user_log).order_by('-project_date')
        obj = project_model.objects.all().filter(user = user_log).order_by('-project_date')
        bookmark_obj = user_bookmark_model.objects.all().filter(user = user_log, bookmark_type = 'Project').order_by('-bookmark_date')

        paginator = Paginator(public_obj, 10)
        paginator_1 = Paginator(obj, 10)            
        paginator_2 = Paginator(bookmark_obj, 10)   

        page_number = request.GET.get('page')
        page_number_1 = request.GET.get('page')   #not working as intended  
        page_number_2 = request.GET.get('page')   #not working as intended  

        page_obj = paginator.get_page(page_number)
        page_obj_1 = paginator_1.get_page(page_number_1)
        page_obj_2 = paginator_2.get_page(page_number_2)

        context = {'user':user_log, 'form':form, 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2 ,'page_obj': page_obj}

        if request.method == 'POST':
            form = project_form(request.POST)

            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.user = user_log
                form_obj.save()
                form = project_form()

                context = {'user':user_log, 'form':form, 'message':'success', 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2, 'page_obj': page_obj}
                return redirect('/user_module/projects')
            else:
                form = project_form()
                context = {'user':user_log, 'form':form, 'message':'Unsuccessfull !!', 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2, 'page_obj': page_obj}
                return render(request, 'projects.html', context)

        return render(request, 'projects.html', context)
    else:
        return redirect(reverse('home:loginpage'))

def projects_detailview(request,pk):
    user_log = request.user

    if user_log.is_authenticated:
        id = pk

        obj = project_model.objects.all().filter(pk=id)
        obj_user = obj.values('user').first()
        obj_id = obj.values('id').first()
        obj_project_name = obj.values('project_name').first()        
        profile_obj = profile_model.objects.filter(user=str(obj_user['user']))
        bookmark_obj = user_bookmark_model.objects.filter(user=str(user_log)
                                                            ,bookmark_name=str(obj_project_name['project_name'])
                                                            ,bookmark_id=str(obj_id['id'])
                                                            ,bookmark_type='Project')

        delete_bookmark_obj = user_bookmark_model.objects.filter(bookmark_name=str(obj_project_name['project_name'])
                                                                ,bookmark_id=str(obj_id['id'])
                                                                ,bookmark_type='Project')

        form = project_form(request.POST or None, instance = obj.first())
        bookmark_form = user_bookmark_form(request.POST or None)

        if bookmark_obj.count()>0:
            bookmark = True
        else:
            bookmark = False

        context = {'user_log':user_log, 'obj':obj, 'profile_obj':profile_obj, 'form':form,
                     'bookmark_form':bookmark_form, 'bookmark':bookmark}

        if 'submit' in request.POST:

            if 'update' == request.POST.get('submit'):

                if form.is_valid():
                    form_obj = form.save(commit=False)
                    form_obj.user = str(user_log)
                    form_obj.save()
                    return redirect('/user_module/projects/'+str(obj_id['id'])+'/')

            elif 'bookmark' == request.POST.get('submit'):

                if bookmark_form.is_valid():
                    bookmark_form_obj = bookmark_form.save(commit=False)
                    bookmark_form_obj.user = str(user_log)
                    bookmark_form_obj.bookmark_type = 'Project'
                    bookmark_form_obj.bookmark_name = str(obj_project_name['project_name'])
                    bookmark_form_obj.bookmark_id = str(obj_id['id'])
                    bookmark_form_obj.save()
                    return redirect('/user_module/projects/'+str(obj_id['id'])+'/')

            elif 'unbookmark' == request.POST.get('submit'):
                bookmark_obj.delete()
                return redirect('/user_module/projects/'+str(obj_id['id'])+'/')

            elif 'yes' == request.POST.get('submit'):
                obj.delete() 
                return redirect('/user_module/projects')      

        return render(request, 'projects_detailview.html', context)
    else:
        return redirect(reverse('home:loginpage'))


def skills(request, *args, **kwargs): 
    user_log = request.user

    if user_log.is_authenticated:
        form = skill_form()

        public_obj = skill_model.objects.all().exclude(user = user_log).order_by('-skill_date')
        obj = skill_model.objects.all().filter(user = user_log).order_by('-skill_date')
        bookmark_obj = user_bookmark_model.objects.all().filter(user = user_log, bookmark_type = 'Skill').order_by('-bookmark_date')


        paginator = Paginator(public_obj, 10)
        paginator_1 = Paginator(obj, 5)              
        paginator_2 = Paginator(bookmark_obj, 5)    

        page_number = request.GET.get('page')
        page_number_1 = request.GET.get('page') #not working as intended
        page_number_2 = request.GET.get('page') #not working as intended

        page_obj = paginator.get_page(page_number)
        page_obj_1 = paginator_1.get_page(page_number_1)
        page_obj_2 = paginator_2.get_page(page_number_2)

        context = {'user':user_log, 'form':form, 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2 ,'page_obj': page_obj}

        if request.method == 'POST':
            form = skill_form(request.POST)

            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.user = user_log
                form_obj.save()
                form = skill_form()

                context = {'user':user_log, 'form':form, 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2, 'page_obj': page_obj, 'message':'success'}
                return redirect('/user_module/skills')
            else:
                form = skill_form()
                context = {'user':user_log, 'form':form, 'page_obj_1':page_obj_1, 'page_obj_2': page_obj_2, 'page_obj': page_obj, 'message':'Unsuccessfull !!'}
                return render(request, 'skills.html',context)

        return render(request, 'skills.html',context)
    else:
        return redirect(reverse('home:loginpage')) 

def skills_detailview(request,pk):
    user_log = request.user

    if user_log.is_authenticated:
        id = pk

        obj = skill_model.objects.all().filter(pk=id)
        obj_user = obj.values('user').first()
        obj_id = obj.values('id').first()
        obj_skill_name = obj.values('skill_name').first()
        profile_obj = profile_model.objects.filter(user=str(obj_user['user']))
        bookmark_obj = user_bookmark_model.objects.filter(user=str(user_log)
                                                            ,bookmark_name=str(obj_skill_name['skill_name'])
                                                            ,bookmark_id=str(obj_id['id'])
                                                            ,bookmark_type='Skill')

        delete_bookmark_obj = user_bookmark_model.objects.filter(bookmark_name=str(obj_skill_name['skill_name'])
                                                                ,bookmark_id=str(obj_id['id'])
                                                                ,bookmark_type='Skill')

        form = skill_form(request.POST or None, instance = obj.first())
        bookmark_form = user_bookmark_form(request.POST or None)
        
        if bookmark_obj.count()>0:
            bookmark = True
        else:
            bookmark = False

        context = {'user_log':user_log, 'obj':obj, 'profile_obj':profile_obj, 'form':form,
                     'bookmark_form':bookmark_form, 'bookmark':bookmark}

        if 'submit' in request.POST:

            if 'update' == request.POST.get('submit'):

                if form.is_valid():
                    form_obj = form.save(commit=False)
                    form_obj.user = str(user_log)
                    form_obj.save()
                    return redirect('/user_module/skills/'+str(obj_id['id'])+'/')

            elif 'bookmark' == request.POST.get('submit'):

                if bookmark_form.is_valid():
                    bookmark_form_obj = bookmark_form.save(commit=False)
                    bookmark_form_obj.user = str(user_log)
                    bookmark_form_obj.bookmark_type = 'Skill'
                    bookmark_form_obj.bookmark_name = str(obj_skill_name['skill_name'])
                    bookmark_form_obj.bookmark_id = str(obj_id['id'])
                    bookmark_form_obj.save()
                    return redirect('/user_module/skills/'+str(obj_id['id'])+'/')

            elif 'unbookmark' == request.POST.get('submit'):
                bookmark_obj.delete()
                return redirect('/user_module/skills/'+str(obj_id['id'])+'/')

            elif 'yes' == request.POST.get('submit'):
                obj.delete() 
                delete_bookmark_obj.delete()
                return redirect('/user_module/skills')      

        return render(request, 'skills_detailview.html', context)
    else:
        return redirect(reverse('home:loginpage'))    
    

def profile(request):
    user_log = request.user

    if user_log.is_authenticated:
        email = user_log.email 
        profile_obj = profile_model.objects.filter(user = user_log)
        context = {'profile_obj':profile_obj}

        if profile_obj.count()>0:
            update_form = profile_form(request.POST, request.FILES, instance = profile_obj.first())

            if request.method == 'POST':
                
                if update_form.is_valid():
                    update_form_obj = update_form.save(commit=False)
                    update_form_obj.user = str(user_log)
                    update_form_obj.save()
                return redirect('/user_module/profile')       
                         
            context = {'profile_obj':profile_obj, 'update_form':update_form}

            return render(request, 'profile.html' , context)

        else:
            form = profile_form()
            context   = {'form':form}  

            if request.method == 'POST':
                form = profile_form(request.POST, request.FILES)

                if form.is_valid():
                    form_obj = form.save(commit=False)
                    form_obj.user = str(user_log)
                    form_obj.email = str(email)
                    form_obj.save()
                return redirect('/user_module/profile')  

            return render(request, 'profile.html' , context)
    else:
        return redirect(reverse('home:loginpage'))

def logout_page(request):
    logout(request)
    return redirect(reverse('home:homepage'))




#redirection from details views
def project_to_project_redirect(request,*args, **kwargs):
    return redirect('/user_module/projects')

def project_to_skill_redirect(request,*args, **kwargs):
    return redirect('/user_module/skills')

def project_to_profile_redirect(request,*args, **kwargs):
    return redirect('/user_module/profile')

def project_to_logout_redirect(request,*args, **kwargs):
    return redirect('/user_module/logout')

def skill_to_project_redirect(request,*args, **kwargs):
    return redirect('/user_module/projects')

def skill_to_skill_redirect(request,*args, **kwargs):
    return redirect('/user_module/skills')

def skill_to_profile_redirect(request,*args, **kwargs):
    return redirect('/user_module/profile')

def skill_to_logout_redirect(request,*args, **kwargs):
    return redirect('/user_module/logout')