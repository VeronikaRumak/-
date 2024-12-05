from django.db import models
from django.core.exceptions import ValidationError


class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class Position(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    positions = models.ManyToManyField('Position', related_name='employees')
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Child(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class TypeReference(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Reference(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процессе'),
        ('ready', 'Готова'),
    ]

    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='references', null=True, blank=True)
    child = models.ForeignKey('Child', on_delete=models.CASCADE, related_name='references', blank=True, null=True)
    type_of_reference = models.ForeignKey('TypeReference', on_delete=models.CASCADE, related_name='references')
    analysis_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        if self.status == 'ready' and (not self.analysis_date or not self.expiration_date):
            raise ValidationError('Даты должны быть заполнены, если статус справки "готова".')
        if self.status == 'in_progress' and (self.analysis_date or self.expiration_date):
            raise ValidationError('Даты должны быть пустыми, если статус справки "в процессе".')
        if not self.client and not self.child:
            raise ValidationError('Одно из полей "Клиент" или "Ребенок" должно быть заполнено.')
        if self.client and self.child:
            raise ValidationError('Только одно из полей "Клиент" или "Ребенок" должно быть заполнено.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client} - {self.type_of_reference}"


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Visiting(models.Model):
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True)
    child = models.ForeignKey('Child', on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    visiting_date = models.DateField(null=False)
    visiting_time = models.TimeField(null=False)
    missed_date = models.DateField(null=True, blank=True)
    rescheduled_date = models.DateField(null=True, blank=True)
    rescheduled_time = models.TimeField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('visiting_date', 'visiting_time')

    def __str__(self):
        return f"{self.visiting_date} {self.visiting_time} - {self.status}"

