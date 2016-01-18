from django import forms


class MainProject(forms.Form):
    project_name = forms.CharField(widget=forms.TextInput)

    def __unicode__(self):
        return "%s" % self.project_name