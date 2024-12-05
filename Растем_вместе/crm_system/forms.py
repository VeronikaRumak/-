from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['login', 'password']
        labels = {
            'login': 'Логин',
            'password': 'Пароль',
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'middle_name', 'phone_number']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество',
            'phone_number': 'Телефон',
        }


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['client', 'first_name', 'last_name', 'middle_name']
        labels = {
            'client': 'Клиент',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].required = True


class ClientReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['client', 'type_of_reference', 'analysis_date', 'expiration_date', 'status', 'comment']
        labels = {
            'client': 'ФИО клиента',
            'type_of_reference': 'Справка',
            'analysis_date': 'Дата сдачи анализов',
            'expiration_date': 'Дата конца действия',
            'status': 'Готовность справки',
            'comment': 'Комментарий',
        }
        widgets = {
            'analysis_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].required = True
        self.fields['type_of_reference'].queryset = TypeReference.objects.all().order_by('type')


class ChildReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['child', 'type_of_reference', 'analysis_date', 'expiration_date', 'status', 'comment']
        labels = {
            'child': 'ФИО ребенка',
            'type_of_reference': 'Справка',
            'analysis_date': 'Дата сдачи анализов',
            'expiration_date': 'Дата конца действия',
            'status': 'Готовность справки',
            'comment': 'Комментарий',
        }
        widgets = {
            'analysis_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child'].required = True
        self.fields['type_of_reference'].queryset = TypeReference.objects.all().order_by('type')


class VisitingForm(forms.ModelForm):
    class Meta:
        model = Visiting
        fields = ['client', 'employee', 'visiting_date', 'visiting_time', 'missed_date', 'rescheduled_date', 'rescheduled_time', 'status', 'comment',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(positions__position='Инструктор')


class VisitingChildForm(forms.ModelForm):
    class Meta:
        model = Visiting
        fields = ['child', 'employee', 'visiting_date', 'visiting_time', 'missed_date', 'rescheduled_date', 'rescheduled_time', 'status', 'comment',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(positions__position='Инструктор')
