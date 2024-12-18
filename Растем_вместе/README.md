# Дипломная работа
### на тему "Разработка crm-системы для спортивно-оздоровительного центра "Растем вместе" на базе фреймворка Django"


## Обзор проекта

Предлагается сделать crm-систему (веб приложение) на базе фреймворка Django, которое позволит пользователям (администраторам, инструкторам) филиалов "Растем вместе" хранить данные в цифровом формате, а не на бумаге (в журналах).
Соответственно, потребуются механизмы авторизации пользователей для разграничения прав.

**Администратор** может добавлять нового клиента/ребенка (ФИО, номер телефона), добавить информацию о готовности справки (для записи на занятия она необходима), добавлять информацию о посещении (расписании для инструкторов).
**Инструктор** может просматривать свое расписание (на стадии разработки).

Для интерфейса использовались css-стили и html-шаблоны. Для хранения данных использовалась среда разработки базы данных PostegreSQL. Для создания таблиц использовались миграции.


## Структура проекта

**Фронтенд**

Проект включает следующие ключевые компоненты:

**Страница авторизации (рисунок 3)**

![Авторизация.png](img_1.png)
Рисунок 3 - Страница авторизации

При вводе логина и пароля происходит проверка правильности введенных данных и есть ли они в базе.

Если есть (и корректно введен) и логин привязан к роли "Инструктор", то открывается главная страница "Инструктора" (рисунок 4).
![Главная страница инструктора](img_2.png)
Рисунок 4 - Главная страница инструктора

Если есть (и корректно введен) и логин привязан к роли "Администратор", то открывается страница "Администратора" (рисунок 5).
![Главная страница администратора](img_4.png)
Рисунок 5 - Главная страница администратора

На данной странице пользователь может добавить нового клиента, добавить ребенка, редактировать клиента, с помощью поиска быстро найти нужного клиента. 

Перейти на страницы:
 - со списком детей (нажав на кнопку "Дети"), 
 - со списком справок (нажав на "Справки"), 
 - со списком посещения занятий (нажав на "Расписание").


**Страница список детей (рисунок 6)**

На данной странице пользователь может добавить запись ребенка, редактировать запись ребенка и вернуть назад (на страницу "Список клиентов"), а также найти ребенка через поисковую строку.
![Страница список детей](img_7.png)
Рисунок 6 - Страница список детей

**Страница создать клиента (рисунок 7)**

Пользователь может ввести ФИО и номер телефона клиента в соответствующие ячейки.
![Страница создать клиента](img_6.png)
Рисунок 7- Страница создать клиента  


**Страница добавления ребенка (рисунок 8)**

На данной странице пользователь может создать запись о ребенке и привязать его к клиенту, который уже внесен в базу.

При нажатии кнопки назад происходи возврат на страницу "Список клиентов".
![Страница добавления ребенка](img_5.png)
Рисунок 8 - Страница добавления ребенка


**Страница редактировать клиента (рисунок 9)**

На данной странице пользователь может редактировать уже созданные данные в базе (необходимо выбрать строку в таблице, а затем нажать на кнопку редактирования).

При нажатии кнопки назад происходи возврат на страницу "Список клиентов".
![Страница редактировать клиента](img_8.png)
Рисунок 9 - Страница редактировать клиента


**Страница редактирования ребенка (рисунок 10)**

На данной странице пользователь может редактировать уже созданные данные в базе (необходимо выбрать строку в таблице, а затем нажать на кнопку редактирования).

При нажатии кнопки назад происходи возврат на страницу "Список детей".
![Страница редактирования ребенка](img_9.png)
Рисунок 10 - Страница редактирования ребенка


**Страница список справок (рисунок 11)**

На данной странице пользователь может добавить запись справки, редактировать запись справки и перейти на страницу ("Список справок для детей"), а также найти клиента по его ФИО, типе справки, дате сдачи анализа, дате конца действия справки через поисковую строку.

![Страница список справок](img_10.png)
Рисунок 11 - Страница список справок


**Страница создания записи справки (рисунок 12)**

На данной странице пользователь может добавить запись справки для клиента.

Если справка находится в процессе (получения), то даты должны быть пустыми, если статус "Готова", то обязательно должны быть прописаны даты.
![Страница создания записи справки](img_11.png)
Рисунок 12 - Страница создания записи справки


При нажатии на поле для ввода даты откроется календарь.
![Страница создания записи справки(календарь)](img_12.png)
Рисунок 13 - Страница создания записи справки (календарь)


**Страница список справок для детей (рисунок 14)**

На данной странице пользователь может добавить запись справки, редактировать запись справки и вернуться назад (перейти на страницу "Список справок"), а также найти ребенка по его ФИО, типе справки, дате сдачи анализа, дате конца действия справки через поисковую строку.

При нажатии на кнопку "Создать справку" открывается аналогичная страница как на рисунке 12 (вместо ФИО клиента - ФИО ребенка).

При нажатии на кнопку "Редактировать справку" открывается аналогичная страница как на рисунке 15 (вместо ФИО клиента - ФИО ребенка).

![Страница список справок для детей](img_13.png)
Рисунок 14 - Страница список справок для детей


**Страница редактирования справки (рисунок 15)**

На данной странице пользователь может редактировать уже созданные данные в базе (необходимо выбрать строку в таблице, а затем нажать на кнопку редактирования).

![Страница редактирования справки](img_14.png)
Рисунок 15 - Страница редактирования справки


**Страница списка посещений (рисунок 16)**

На данной странице пользователь может добавить запись посещения, редактировать запись посещения и перейти на страницу "Список посещения детей", а также найти клиента по его ФИО, ФИО инструктора, дате прихода, времени прихода через поисковую строку.

Выпадающий список времени аналогичный как на рисунке 18.
![Страница списка посещений](img_15.png)
Рисунок 16 - Страница списка посещений


**Страница добавления посещения (рисунок 17)**

На данной странице пользователь может добавить запись посещения.

![Страница добавления посещения](img_16.png)
Рисунок 17 - Страница добавления посещения

При нажатии на поле ввода времени выпадает список для настройки времени.

При нажатии на поле ввода даты открывается календарик как на рисунке 13.
![Страница добавления посещения(список времени)](img_17.png)
Рисунок 18 - Страница добавления посещения(список времени)

На данной странице пользователь может редактировать уже созданные данные в базе (необходимо выбрать строку в таблице, а затем нажать на кнопку редактирования).

![Страница редактирования посещения клиента](img_18.png)
Рисунок 19 - Страница редактирования посещения клиента


**Страница список посещений детей (рисунок 20)**

При нажатии на кнопку "Добавить посещение ребенка" открывается аналогичная страница как на рисунке 17 (вместо ФИО клиента - ФИО ребенка).

При нажатии на кнопку "Редактировать" открывается аналогичная страница как на рисунке 19 (вместо ФИО клиента - ФИО ребенка).

![img_19.png](img_19.png)
Рисунок 20 - Страница список посещений детей


**Бэкенд**

Реализована серверная логика с использованием фреймворка Django.

Настроены маршруты для вывода данных, добавления данных, редактирование данных.

**Файловая структура приложения**
```
├───crm_system
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   0002_rename_id_type_of_reference_reference_type_of_reference.py
│   │   │   0003_alter_reference_client.py
│   │   │   0004_position_employee_delete_users.py
│   │   │   0005_status.py
│   │   │   0006_visiting.py
│   │   │   0007_alter_status_status.py
│   │   │   0008_alter_status_status.py
│   │   │   0009_alter_status_status.py
│   │   │   0010_alter_visiting_unique_together.py
│   │   │   __init__.py
│
├───static
│   └───css
│           styles.css
│
├───templates
│   │   admin_home.html
│   │   authorization.html
│   │   base.html
│   │   instructor_home.html
│   │
│   ├───create
│   │   ├───list
│   │   │       create_child.html
│   │   │       create_client.html
│   │   │
│   │   ├───reference
│   │   │       create_reference.html
│   │   │       create_reference_child.html
│   │   │
│   │   └───visiting
│   │           add_child_visiting.html
│   │           add_client_visiting.html
│   │
│   ├───edit
│   │   ├───list
│   │   │       edit_child.html
│   │   │       edit_client.html
│   │   │
│   │   ├───reference
│   │   │       edit_reference.html
│   │   │       edit_reference_child.html
│   │   │
│   │   └───visiting
│   │           edit_child_visiting.html
│   │           edit_client_visiting.html
│   │
│   └───list
│       ├───list
│       │       child_list.html
│       │
│       ├───reference
│       │       reference_child_list.html
│       │       reference_list.html
│       │
│       └───visiting
│               visiting_child_list.html
│               visiting_list.html
│
└───Растем_вместе
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
```


## Основные моменты для работы с кодом


Что бы заполнить главные таблицы (Employee (для авторизации), Position (должности), Role (роли), TypeReference(типы справок)) необходимо:
1. Сделать миграцию (```python manage.py makemigrations
                        python manage.py migrate```);


2. Потом необходимо создать пользователя, который на сервере на странице администрирования (сервер/admin) сможет добавить данные в главные таблицы (и не только в них) - ```python manage.py createsuperuser```;


Данные таблицы и вся структура базы данных находится в файле models.py.

Не забудьте в PostegreSQL (pgAdmin) создать сервер и в settings.py поменять название сервера и другие параметры.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_data_base_name',
        'USER': 'your_user_name',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

После создания данных можно открыть страницу авторизации (просто запустив сервер оно по умолчанию откроется). В зависимости от роли пользователя откроются разные страницы (рисунок 4, 5). 
На листинге 1 продемонстрирована функция, которая через запрос проверяет роль и открывает соответствующие страницы.

Листинг 1 - Функция проверки роли пользователя и функция маршрутизации страниц после авторизации.
```
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
```

Данные функции прописаны в файле views.py, в котором прописываются представления (маршрутизация и что будет происходить при том или ином действии).


Для выделения строк в таблицах (и для дальнейшего редактирования даннных) была использована команда <script>, которая прописывается в <body> html-шаблонов. На листинге 2 представлен код.

Листинг 2 - Запрос в html-шаблоне для выделения строки таблицы(для редактирования).
```
<script>
        let selectedRow = null;

        document.querySelectorAll('#client-table tbody tr').forEach(row => {
            row.addEventListener('click', () => {
                if (selectedRow) {
                    selectedRow.classList.remove('selected');
                }
                selectedRow = row;
                row.classList.add('selected');
            });
        });

        function editSelectedClient() {
            if (selectedRow) {
                const clientId = selectedRow.getAttribute('data-id');
                window.location.href = `{% url 'edit_client' 0 %}`.replace('/0', `/${clientId}`);
            } else {
                alert('Пожалуйста, выберите строку для редактирования клиента.');
            }
        }
    </script>
```


Чтобы выводить данные в таблицах (определенные данные, в другом виде) используются формы, которые прописываются в файле forms.py. На листинге 3 представлен одна из форм для таблицы справок детей.

Листинг 3 - Форма справки детей (ChildReferenceForm)
```
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
```
