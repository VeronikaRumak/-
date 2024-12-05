"""
URL configuration for Растем_вместе project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from crm_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),

    path('admin_home/', views.admin_home, name='admin_home'),
    path('instructor_home/', views.instructor_home, name='instructor_home'),

    path('create_client/', views.create_client, name='create_client'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),

    path('create_child/', views.create_child, name='create_child'),
    path('child_list/', views.child_list, name='child_list'),
    path('edit_child/<int:child_id>/', views.edit_child, name='edit_child'),

    path('references/', views.reference_list, name='reference_list'),
    path('references/create/', views.create_reference, name='create_reference'),
    path('references/edit/<int:reference_id>/', views.edit_reference, name='edit_reference'),
    path('references/children/', views.reference_child_list, name='reference_child_list'),
    path('references/children/create/', views.create_reference_child, name='create_reference_child'),
    path('references/children/edit/<int:reference_id>/', views.edit_reference_child, name='edit_reference_child'),

    path('visiting_list/', views.visiting_list, name='visiting_list'),
    path('add_client_visiting/', views.add_client_visiting, name='add_client_visiting'),
    path('edit_client_visiting/<int:visit_id>/', views.edit_client_visiting, name='edit_client_visiting'),
    path('visiting_child_list/', views.visiting_child_list, name='visiting_child_list'),
    path('add_child_visiting/', views.add_child_visiting, name='add_child_visiting'),
    path('edit_child_visiting/<int:visit_id>/', views.edit_child_visiting, name='edit_child_visiting'),
]

