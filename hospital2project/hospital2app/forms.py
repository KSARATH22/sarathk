from django import forms


class DocterForm(forms.Form):
    first_name=forms.CharField(
        label="Enter first Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'your first name'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your last name'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Mobile Num",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your number'
            }
        )
    )
    addres=forms.CharField(
        label="Enter Addres",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your addres'
            }
        )
    )
class PatientsForm(forms.Form):
    first_name=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    pat_age=forms.IntegerField(
        label="Enter Your Age",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter age',
            }
        )
    )
    pat_gender=forms.CharField(
        label="Enter Gender",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter gender',
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Mobile Num",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your number'
            }
        )
    )

    addres = forms.CharField(
        label="Enter Addres",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your addres'
            }
        )
    )

class NursesForm(forms.Form):
    first_name = forms.CharField(
        label="Enter first Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your first name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your last name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Mobile Num",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your number'
            }
        )
    )
    addres = forms.CharField(
        label="Enter Addres",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your addres'
            }
        )
    )
class ReportsForm(forms.Form):
    case=forms.CharField(
        label="Enter PatientCase",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your case'
            }
        )
    )
    lab_attendant=forms.CharField(
        label="Enter LabAttendance",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter lab_attendance'
            }
        )
    )
    generated_date=forms.DateField(
        label="Enter Date",
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter date here'
            }
        )
    )
    description=forms.CharField(
        label="Enter Description",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your description'
            }
        )
    )
class MessagesForm(forms.Form):
    name=forms.CharField(
        label="Enter Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }
        )
    )

    message=forms.CharField(
        label="Enter Your Message",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Message'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Rating'
            }
        )
    )
class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='Enter First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'first Name'
            }
        )
    )
    last_name = forms.CharField(
        label='Enter Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'last Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'EmailId'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile'
            }
        )
    )

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Rating:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )

