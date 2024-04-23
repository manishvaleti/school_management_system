from django import forms
from .models import *

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        } 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'age', 'phone']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'subject_name':forms.TextInput(attrs={'class':'form-control'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_count','class_time', 'teacher', 'subject']
        widgets = {
            'class_count': forms.TextInput(attrs={'class': 'form-control'}),
            'class_time':forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Staff.objects.all()
        self.fields['subject'].queryset = Subject.objects.all()

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student','total_amount', 'due_amount', 'paid_amount', 'payment_date', 'due_date']
        widgets = {
            'total_amount':forms.TextInput(attrs={'class': 'form-control'}),
            'due_amount':forms.TextInput(attrs={'class': 'form-control'}),
            'paid_amount':forms.TextInput(attrs={'class': 'form-control'}),
            'payment_date':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'due_date':forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'student':forms.Select(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()

class ClassRegisterForm(forms.ModelForm):
    class Meta:
        model = ClassRegister
        fields = ['student','classes']
        widgets = {
            'student':forms.Select(attrs={'class':'form-control'}),
            'classes':forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add queryset for dropdowns
        self.fields['classes'].queryset = Class.objects.all()
        self.fields['student'].queryset = Student.objects.all()

class UpdateMarkForm(forms.ModelForm):
    class Meta:
        model = ClassRegister
        fields = ['marks']
        widgets = {
            'marks': forms.TextInput(attrs={'class':'form-control'}),
        }