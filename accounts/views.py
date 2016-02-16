
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from accounts.forms import RegisterProfileForm, RegisterUserForm
from accounts.models import UserProfile

class RegisterView(FormView):
    template_name = "register.html"


    def get(self, request, *args, **kwargs):
        formUser = RegisterUserForm()
        formProfile = RegisterProfileForm()
        ctx = {
            'formusr': formUser,
            'formprofile':formProfile
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
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
            message = 'Se agrego correctamente'
            ctx['message']=message

            return render(request,self.template_name,ctx)
        else:
            return render(request,self.template_name,ctx)

class ProfileView(FormView):
    template_name = "profile.html"

    # @method_decorator(login_required(login_url='/inicio_de_sesion'))
    # def get(self, request, *args, **kwargs):
    #     # formAccount = EditAccountForm(request.user, request.POST)
    #     # if formAccount.is_valid():
    #     #     ctx = {'formAccount':formAccount}
    #     #     return render(request,self.template_name,ctx)



    def post(self, request, *args, **kwargs):
        usermodel = UserProfile.objects.all()
        ctx = {
            'model':usermodel,
        }
        return render(request,self.template_name,ctx)
