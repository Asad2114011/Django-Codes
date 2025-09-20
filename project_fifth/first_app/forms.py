from django import forms
from django.core import validators
class contactForm(forms.Form):
    name=forms.CharField(label="Full name:",help_text="Total length must be contain 40 character",
        required=False,widget=forms.Textarea(attrs={'id':'text_area','class':'class1','placeholder':'Enter your name'}) )
    file=forms.FileField()
    email=forms.EmailField(label="user email")
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.CharField(widget=forms.DateTimeInput(attrs={'type' : 'datetime-local'}))
    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal=[('p','pepperoni'),('m','mashroom'),('b','beef')]
    pizza=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)


# class studentData(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     age=forms.CharField()
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname)<7:
#     #         raise forms.ValidationError("Enter a name with at least 7 characters")
#     #     return valname
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("your email must contain .com")
        
#     def clean(self):
#         cleaned_data=super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname)<7:
#             raise forms.ValidationError("Eneter a name with at least 7 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a value at least 10 character")
    
class studentData(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email")])
    age=forms.IntegerField(widget=forms.NumberInput,validators=[validators.MaxValueValidator(34,message="age must be at most 34"),validators.MinValueValidator(24,message="age must be at least 24")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="File extension must be ended with .pdf")])

class passwordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['confirm_password']
        valname=self.cleaned_data['name']
        if val_pass!=val_conpass:
            raise forms.ValidationError("Password doesnt match")
        if len(valname)<10:
            raise forms.ValidationError("Name must be at least 10 characters")