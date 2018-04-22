"""pandjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from website.views import StartView, ContactView, SmsFormView, BoardView
from accounts.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name='index'),
    path('contact', ContactView.as_view(), name='contact'),
    path('sms', SmsFormView.as_view(), name='sms'),
    path('board', BoardView.as_view(), name='board'),
    path('dossier/', include('dossier.urls'), name='dossier'),
    path('blog/', include('blog.urls'), name='blog'),
    #acconts
    path('signup', signup, name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(template_name = 'login.html'), name='login'),

    path('reset',
        PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    path('reset/done',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    path('settings/password', PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    path('settings/password/done', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
]

