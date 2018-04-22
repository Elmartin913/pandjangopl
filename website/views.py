from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.template.response import TemplateResponse

from .models import  Contact, Sms
from .forms import ContactForm, SmsForm
#from .send_sms import client
# Create your views here.

class StartView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')


class ContactView(View):
    def get(self,request):
        form = ContactForm()
        return render(request, 'contact_form.html', {'form':form, 'send': 0})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            new_contact = Contact.objects.create(
                message=message,
                name=name,
                email=email,
                mobile=mobile,
            )
            return render(request, 'contact_form.html', { 'send': 1})

        #return HttpResponse('wiadomość nie zapisana')
        return render(request, 'contact_form.html', {'form': form, 'send': 0})

        #return HttpResponseRedirect('')


class BoardView(LoginRequiredMixin, View):
    def get(self, request):
        contacts = Contact.objects.all().order_by('-id')
        return render(request, 'board.html', {'contacts': contacts})


class SmsFormView(View):
    def get(self, request):
        form  = SmsForm
        ctx = {'send':0, 'form': form}
        return render(request, 'sms_form.html', ctx)

    def post(self, request):
        form = SmsForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['body']
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            Sms.objects.create(
                name=name,
                mobile=mobile,
                body=body,
                sms_send=True,
            )

            body2 = '{}-{}-{}'.format(name, mobile, body)
            client.api.account.messages.create(
                to="+48793979913",
                from_="+48732168077",
                body=body2,
            )
            direct = [45,50,51,53,57,60,66,69,72,73,78,79,88]
            print(int(mobile[:2]))
            if len(mobile)==9 and int(mobile[:2]) in direct:
                to = "+48{}".format(mobile)


                client.api.account.messages.create(
                    to=to,
                    from_="+48732168077",
                    body="Życzę miłego dnia. PanDjango :)",
                )
                
            
            
            return render(request, 'sms_form.html', {'send': 1})

        return render(request, 'sms_form.html', {'send':0, 'form': form})