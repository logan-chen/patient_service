from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegister(forms.Form):
    pass


class PatientRegister(forms.Form):
    recommend_id = forms.CharField(widget=forms.TextInput)
    name = forms.CharField(widget=forms.TextInput, required=True)
    age = forms.CharField(widget=forms.TextInput, required=True)
    gender = forms.CharField(widget=forms.TextInput, required=True)
    phone = forms.CharField(widget=forms.TextInput, required=True)
    weight = forms.CharField(widget=forms.TextInput, required=True)
    height = forms.CharField(widget=forms.TextInput, required=True)
    disease_info = forms.CharField(widget=forms.TextInput, required=True)
    treatment_info = forms.CharField(widget=forms.TextInput, required=True)
    family = forms.CharField(widget=forms.TextInput, required=True)
    o_contact = forms.CharField(widget=forms.TextInput, required=True)
    city_info = forms.CharField(widget=forms.TextInput, required=True)
    case_img = forms.FilePathField(widget=forms.FilePathField, required=True)


class DoctorRegister(forms.Form):
    phone = forms.CharField(widget=forms.TextInput, required=True)
    recommend_id = forms.CharField(widget=forms.TextInput)
    nikename = forms.CharField(widget=forms.TextInput)
    age = forms.CharField(widget=forms.TextInput, required=True)
    contact_number = forms.CharField(widget=forms.TextInput, required=True)
    department = forms.CharField(widget=forms.TextInput, required=True)
    affiliated_hospital = forms.CharField(widget=forms.TextInput, required=True)
    o_contact = forms.CharField(widget=forms.TextInput, required=True)


class EnterPriseRegister(forms.Form):
    phone = forms.CharField(widget=forms.TextInput, required=True)
    e_name = forms.CharField(widget=forms.TextInput, required=True)
    department = forms.CharField(widget=forms.TextInput, required=True)
    contact_number = forms.CharField(widget=forms.TextInput, required=True)
    email = forms.CharField(widget=forms.TextInput, required=True)
    position = forms.CharField(widget=forms.TextInput)
    products = forms.CharField(widget=forms.TextInput)
    address = forms.CharField(widget=forms.TextInput, required=True)
    o_contact = forms.CharField(widget=forms.TextInput, required=True)
