from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils import http
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from accounts.forms import RegisterProfileForm, UserForm
from accounts.models import UserProfile

#----------------------------- Vista para agregar nuevo usuario ---------------------------------#

class RegisterView(FormView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        formUser = UserForm()
        formProfile = RegisterProfileForm()
        ctx = {
            'formusr': formUser,
            'formprofile':formProfile
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        # formUser = RegisterFormUser(request.POST)
        formProfile = RegisterProfileForm(request.POST, request.FILES)
        ctx = {
            'formprofile':formProfile
        }
        if formProfile.is_valid():
            username = formProfile.cleaned_data["username"]
            password = formProfile.cleaned_data["password"]
            first_name = formProfile.cleaned_data["first_name"]
            last_name = formProfile.cleaned_data["last_name"]
            email = formProfile.cleaned_data["email"]

            new_user = User.objects.create_user(username, email, password)

            new_user.last_name = last_name
            new_user.first_name = first_name
            new_user.save()

            new_profile = formProfile.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            message = 'se agrego con exito.'
            ctx['message']=message
            #return render(request,self.template_name,ctx)
            # messages
            messages.add_message(request, messages.INFO, 'Usuario agregado correctamente.')
            return HttpResponseRedirect('/inicio_de_sesion/')
        else:
            return render(request,self.template_name,ctx)

#----------------------------- Vista para el perfil de usuario -------------------------------------#

class ProfileView(FormView):
    template_name = "profile.html"

    @method_decorator(login_required(login_url='/inicio_de_sesion'))
    def get(self, request, *args, **kwargs):
        try:
            user_form = UserForm(instance=request.user)
            profile = UserProfile.objects.filter(user=request.user)
        except User.DoesNotExist:
            raise Http404
        ctx = {'user_form':user_form,
               'profile':profile}
        return render(request,self.template_name,ctx)


#---------------------------- Vista para editar usuario -----------------------------------#
class EditProfileView(FormView):
    template_name = 'editProfile.html'

    def get(self, request, *args, **kwargs):
        try:
            user_form = RegisterProfileForm(instance=request.user)
        except User.DoesNotExist:
            raise Http404
        ctx = {'user_form':user_form}
        return render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        try:
            user_form = RegisterProfileForm(request.POST, instance=request.user)
        except User.DoesNotExist:
            raise Http404
        ctx = {'user_form':user_form}
        return render(request,self.template_name,ctx)