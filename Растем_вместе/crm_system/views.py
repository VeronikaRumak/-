from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from datetime import datetime, timedelta, time as dt_time


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            try:
                user = Employee.objects.get(login=login, password=password)
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role.role

                if user.role.role == 'Администратор':
                    return redirect('admin_home')
                elif user.role.role == 'Инструктор':
                    return redirect('instructor_home')
                else:
                    return redirect('login')

            except Employee.DoesNotExist:
                print("Пользователь не найден или неверно введен пароль")

    else:
        form = LoginForm()

    return render(request, 'authorization.html', {'form': form})


def home_view(request):
    user_role = request.session.get('user_role')

    if user_role == 'Администратор':
        return render(request, 'admin_home.html')
    elif user_role == 'Инструктор':
        return render(request, 'instructor_home.html')
    else:
        return redirect('login')


def admin_home(request):
    query = request.GET.get('q')

    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(children__first_name__icontains=query) |
            Q(children__last_name__icontains=query) |
            Q(children__middle_name__icontains=query)
        ).distinct()

    else:
        clients = Client.objects.all()

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'admin_home.html', {'clients': clients, 'user': user})


def instructor_home(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'instructor_home.html', {'user': user})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ClientForm()

    return render(request, 'create/list/create_client.html', {'form': form})


def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ClientForm(instance=client)

    return render(request, 'edit/list/edit_client.html', {'form': form})


def create_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ChildForm()

    return render(request, 'create/list/create_child.html', {'form': form})


def child_list(request):
    query = request.GET.get('q')

    if query:
        children = Child.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query)
        )
    else:
        children = Child.objects.all()

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'list/list/child_list.html', {'children': children, 'user': user})


def edit_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('child_list')
    else:
        form = ChildForm(instance=child)

    return render(request, 'edit/list/edit_child.html', {'form': form})


def reference_list(request):
    query = request.GET.get('q')
    type_query = request.GET.get('type')
    analysis_date_query = request.GET.get('analysis_date')
    expiration_date_query = request.GET.get('expiration_date')

    references = Reference.objects.filter(client__isnull=False)

    if query:
        references = references.filter(
            Q(client__last_name__icontains=query) |
            Q(client__first_name__icontains=query) |
            Q(client__middle_name__icontains=query)
        )
    if type_query:
        references = references.filter(type_of_reference__type__icontains=type_query)
    if analysis_date_query:
        references = references.filter(analysis_date=analysis_date_query)
    if expiration_date_query:
        references = references.filter(expiration_date=expiration_date_query)

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'list/reference/reference_list.html', {'references': references, 'user': user})


def create_reference(request):
    if request.method == 'POST':
        form = ClientReferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = ClientReferenceForm()

    return render(request, 'create/reference/create_reference.html', {'form': form})


def edit_reference(request, reference_id):
    reference = get_object_or_404(Reference, id=reference_id)
    if request.method == 'POST':
        form = ClientReferenceForm(request.POST, instance=reference)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = ClientReferenceForm(instance=reference)

    return render(request, 'edit/reference/edit_reference.html', {'form': form})


def reference_child_list(request):
    query = request.GET.get('q')
    type_query = request.GET.get('type')
    analysis_date_query = request.GET.get('analysis_date')
    expiration_date_query = request.GET.get('expiration_date')

    references = Reference.objects.filter(child__isnull=False)

    if query:
        references = references.filter(
            Q(child__last_name__icontains=query) |
            Q(child__first_name__icontains=query) |
            Q(child__middle_name__icontains=query)
        )
    if type_query:
        references = references.filter(type_of_reference__type__icontains=type_query)
    if analysis_date_query:
        references = references.filter(analysis_date=analysis_date_query)
    if expiration_date_query:
        references = references.filter(expiration_date=expiration_date_query)

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'list/reference/reference_child_list.html', {'references': references, 'user': user})


def create_reference_child(request):
    if request.method == 'POST':
        form = ChildReferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_child_list')
    else:
        form = ChildReferenceForm()

    return render(request, 'create/reference/create_reference_child.html', {'form': form})


def edit_reference_child(request, reference_id):
    reference = get_object_or_404(Reference, id=reference_id)
    if request.method == 'POST':
        form = ChildReferenceForm(request.POST, instance=reference)
        if form.is_valid():
            form.save()
            return redirect('reference_child_list')
    else:
        form = ChildReferenceForm(instance=reference)

    return render(request, 'edit/reference/edit_reference_child.html', {'form': form})


def visiting_child_list(request):
    query = request.GET.get('child_name')
    employee_query = request.GET.get('employee_name')
    date_query = request.GET.get('visiting_date')
    time_query = request.GET.get('visiting_time')

    visits = Visiting.objects.filter(child__isnull=False)

    if query:
        visits = visits.filter(
            Q(child__last_name__icontains=query) |
            Q(child__first_name__icontains=query) |
            Q(child__middle_name__icontains=query)
        )
    if employee_query:
        visits = visits.filter(
            Q(employee__last_name__icontains=employee_query) |
            Q(employee__first_name__icontains=employee_query) |
            Q(employee__middle_name__icontains=employee_query)
        )
    if date_query:
        visits = visits.filter(visiting_date=date_query)
    if time_query:
        visits = visits.filter(visiting_time=time_query)

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'list/visiting/visiting_child_list.html', {'visits': visits, 'user': user})


def add_child_visiting(request):
    if request.method == 'POST':
        form = VisitingChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visiting_child_list')
    else:
        form = VisitingChildForm()

    return render(request, 'create/visiting/add_child_visiting.html', {'form': form})


def edit_child_visiting(request, visit_id):
    visit = get_object_or_404(Visiting, id=visit_id)
    if request.method == 'POST':
        form = VisitingChildForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visiting_child_list')
    else:
        form = VisitingChildForm(instance=visit)

    return render(request, 'edit/visiting/edit_child_visiting.html', {'form': form, 'visit': visit})


def visiting_list(request):
    query = request.GET.get('client_name')
    employee_query = request.GET.get('employee_name')
    date_query = request.GET.get('visiting_date')
    time_query = request.GET.get('visiting_time')

    visits = Visiting.objects.filter(client__isnull=False)

    if query:
        visits = visits.filter(
            Q(client__last_name__icontains=query) |
            Q(client__first_name__icontains=query) |
            Q(client__middle_name__icontains=query)
        )
    if employee_query:
        visits = visits.filter(
            Q(employee__last_name__icontains=employee_query) |
            Q(employee__first_name__icontains=employee_query) |
            Q(employee__middle_name__icontains=employee_query)
        )
    if date_query:
        visits = visits.filter(visiting_date=date_query)
    if time_query:
        visits = visits.filter(visiting_time=time_query)

    user_id = request.session.get('user_id')
    user = get_object_or_404(Employee, id=user_id)

    return render(request, 'list/visiting/visiting_list.html', {'visits': visits, 'user': user})


def add_client_visiting(request):
    if request.method == 'POST':
        form = VisitingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visiting_list')
    else:
        form = VisitingForm()

    return render(request, 'create/visiting/add_client_visiting.html', {'form': form})


def edit_client_visiting(request, visit_id):
    visit = get_object_or_404(Visiting, id=visit_id)
    if request.method == 'POST':
        form = VisitingForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visiting_list')
    else:
        form = VisitingForm(instance=visit)

    return render(request, 'edit/visiting/edit_client_visiting.html', {'form': form, 'visit': visit})
