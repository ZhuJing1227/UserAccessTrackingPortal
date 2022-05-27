from django.forms import ModelForm
from .models import employee,access, history, Grant
from django import forms


#manage user form
class manageuserform(ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        exclude = ['employeePassword']

#register form
class registerform(ModelForm):
    class Meta:
        model = employee
        fields ='__all__'

#search user form
class findemployee(forms.Form):
    employeename = forms.CharField()

#login form
class loginform(ModelForm):
    class Meta:
        model = employee
        fields = ['employeeEmail','employeePassword']

#change password form
class changepasswordform(ModelForm):
    class Meta:
        model = employee
        fields = ['employeePassword']

#grant access form
class grantaccessform(ModelForm):
    class Meta:
        model = access
        fields = '__all__'

#edit access form
class editaccessform(ModelForm):
    class Meta:
        model = access
        fields = ['accessName','notes']

#history form
class historyform(ModelForm):
    class Meta:
        model = history
        fields = '__all__'