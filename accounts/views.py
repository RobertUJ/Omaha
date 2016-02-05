
from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import RegisterFormProfile, RegisterFormUser
from accounts.models import UserProfile


class RegisterView(FormView):
    template_name = "register.html"


    def get(self, request, *args, **kwargs):
        formUser = RegisterFormUser()
        formProfile = RegisterFormProfile()
        ctx = {
            'formusr': formUser,
            'formprofile':formProfile
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        formUser = RegisterFormUser(request.POST)
        formProfile = RegisterFormProfile(request.POST)
        ctx = {
            'formusr': formUser,
            'formprofile':formProfile
        }
        if formUser.is_valid() and formProfile.is_valid():
            new_user = formUser.save()
            new_profile = formProfile.save(commit=False)
            new_profile.user = new_user
            new_profile.save()



            return render(request,self.template_name,ctx)
        else:
            # print form.e
            return render(request,self.template_name,ctx)