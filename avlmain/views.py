from __future__ import print_function

import os

from django.contrib.auth import logout, login
from googleapiclient.discovery import build

from google.oauth2 import service_account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.files.base import ContentFile

from django.db.models import Q
from .forms import *
from .models import *
from .utils import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def update():
#     SCOPES = [
#
#         'https://www.googleapis.com/auth/spreadsheets',
#
#         'https://www.googleapis.com/auth/drive'
#
#     ]
#
#     credentials = service_account.Credentials.from_service_account_file(
#         'credentials.json', scopes=SCOPES)
#
#     spreadsheet_service = build('sheets', 'v4', credentials=credentials)
#
#     drive_service = build('drive', 'v3', credentials=credentials)
#
cred = {
  "type": "service_account",
  "project_id": "email-list-392809",
  "private_key_id": "9bae0b45d53316a6effa768ba8537c4eb99ca969",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCsFv6siOX8p9sM\nd1dUTQS+RMCATH9sFnniUVrO6KFkAiUy93prfkvPjYFGWmKOUu+rldNExaZ9FqCP\n75pK/5YdufB0kgNYPmI+/sSpFoKGUrEo9oRbxOhAD4EQGu+Fcz7HDXbPQbl1cnmz\nub5DVnb0lbW4mawEavBJ0GUpOK3sAwPdQfOb+d10oDglAZMMJryjqE7QUxeMWxkq\nGmuo8tE8bRl63tyOAbsbrAMdz+z6tdpE+THFh8/xik2UbMAlyeruhhUKarzwFhsW\nE3/OeH4haLwV+bUlK6usmK4NLXcxcmH3SIuxYh4Vu+e1KlHX6XZKwSkUvThKuXtt\n4S04iMytAgMBAAECggEARvNEFMZsa/qYqU8axjrq1bdq1nqznlC198Uq91uaDq2D\nwLuf0WnEv9HLlsH1GFDBV7Dx5czHk5Mcp7tVlc5Cigb7SFRa5Krzvp0zX7NUJSU6\nvXTFpUBNsPuzbnxsfEzDeTXn4hNq7y0/WAYgl4qyiKygu3dAIKImZ4hv7MrdigwW\n37m53WfQ9vTGlUBnosc3kwSjBrXSGxgEuOom2BYP/ZWDYC3sc76fkhEOb50stP31\njUoKiEIRQOjbt41DOrOjmk5ySrZUMM5k/mft5SuQ/iEqEYSpAuEp6uYIkKU7u0gv\n67FMBaRIoqicUFgUQSfitjXXnY+WUP2xguzQzcNq0QKBgQDdMr30x6iQEqX9agcQ\nbt+igXG47kFDr7L1og54GMrI891c5/Rs57V/0bPbBnZAQ4X/nqRJmn0vH8mQhaiG\nDqxlwwid6twCmQyAHVVbRLDA6c2QMFIHZIHCUItfkjoFVl4MAPfguNTJj9YN8Xqt\naxY95TV5A45JbkbWAV+c0W4SWwKBgQDHKk0uGKGpQj2PL3x0G3NYMGxEcmBrhT6E\n64oKNG9a+ttLvGbPl1Y+PQpODvqCly0GiuXBEttkpbIQ6/eNWirWob/4a3YHZP9R\nZ4JpsP2cAKv1Vi+OdA0yRkLcfv0uUSHMDZKmlbYpmEQ53UNwMK4LM9s30qjQT1qi\nFT5CkvM7lwKBgQCAMutzFdB1B8naUHwdoxTL21fsxXFf6FHBGRZntn647tWKBglc\noQJJPWGO/HTGlBvyZaBz5CzPhg3NTBm68IAsTlgNJlQy0T80dUvGJM6IUDlKaybv\nj+nAk+vjDR3BgCfrrxf6z0TMOSfnVuAx6BGw98oBA/WQS3CUkaE3gw3XZwKBgDRK\np/79WpytFqqchimZ93vlItgJy8UPM+4ERbcOM1qI2MEW00uX6X3n2ufJyP42oQzB\ntTcvM0lGs+z7d4C2dt7pkxSvakrguqRt7/C+Fqg6COweV9goIjrb9bwc326kwKHp\nwmJYln5vSyKCNK2lKl0onVsXxVkELMC3oSQrnw87AoGBANUjIpuj3x7xd1p0pE3a\n8S5t/72ysTxbI46fYDlfjw427wxQgOoJYP8LuIGltzlJua3479d1vVEVO7oaGjke\nzDP6OfYqTUqdebneaAc0wEoIQmfJ0AgtL6xfqPdxdHiRzW9bL8RBjBYChXSIN5Pa\n1pAmP3jpqORbMRS5tvQj0pD5\n-----END PRIVATE KEY-----\n",
  "client_email": "python-test@email-list-392809.iam.gserviceaccount.com",
  "client_id": "105933983438990970267",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-test%40email-list-392809.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

email_list = [[]]
def save(value):
    SCOPES = [

        'https://www.googleapis.com/auth/spreadsheets',

        'https://www.googleapis.com/auth/drive'

    ]

    credentials = service_account.Credentials.from_service_account_info(
        cred, scopes=SCOPES)

    spreadsheet_service = build('sheets', 'v4', credentials=credentials)

    drive_service = build('drive', 'v3', credentials=credentials)
    def read_range():
        range_name = 'Sheet1!A1:H10'  # retrieve data from existing sheet
        spreadsheet_id = '1_rK5CFa3JFto4JFwmxnS1KfKh9JAwNa1UDkduE2Wv1c'
        result = spreadsheet_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print('{0} rows retrieved.'.format(len(rows)))
        print('{0} rows retrieved.'.format(rows))
        return rows

    def write_range():
        # f = open('emails.txt', 'r+')
        # data=f.read
        # print(data)

        spreadsheet_id = '1_rK5CFa3JFto4JFwmxnS1KfKh9JAwNa1UDkduE2Wv1c'  # get the ID of the existing sheet
        range_name = 'Sheet1!A2:Z2'  # the range to update in the existing sheet  # new row of data
        value_input_option = 'USER_ENTERED'
        email_list[0].append(value)
        print(email_list)
        body = {
            'values': email_list

        }
        result = spreadsheet_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))

    write_range()
    read_range()

class HomePage(DataMixin, ListView):
    model = Items
    template_name = 'root/home.html'
    data = Items.objects.all()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='A-V-L')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ManClothing(DataMixin, ListView):
    model = Items
    template_name = 'root/man.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Men')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Items.objects.filter(key__slug=self.kwargs['post_slug'])

class ManClothingBase(DataMixin, ListView):
    model = Items
    template_name = 'root/man.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Men')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WomenClothing(DataMixin, ListView):
    model = Items
    template_name = 'root/women.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Women')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'root/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='A-V-L')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'root/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='A-V-L')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowClothes(DataMixin, DetailView):
    model = Items
    template_name = 'root/show_clothes.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['A-V-L'])
        return dict(list(context.items())+list(c_def.items()))


class AboutUs(DataMixin, FormView):
    model = Items
    form_class = ContactForm
    template_name = 'root/about.html'

    def form_valid(self, form):
        print(form.cleaned_data)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='A-V-L')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# def form_add(request):
# class AboutUs(DataMixin, FormView):
#     model = Items
#     template_name = 'root/about.html'
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='A-V-L')
#         context = dict(list(context.items()) + list(c_def.items()))
#         return context

def about(request):
    contact_list = Items.objects.all()
    context = {
               'menu': menu,
               'title': 'A-V-L',
               }
    menu2 = [
             {'title': "CART", 'url_name': 'cart'},]
    context['menu2'] = menu2

    if request.method == 'POST':
        print(request.POST['email'])
        save(request.POST['email'])

    return render(request, 'root/about.html', context)


def search(request):
    query = request.GET.get('q', '')
    print(query)
    if query:
        results = Items.objects.filter(Q(name__icontains=query) | Q(slug__icontains=query))
    else:
        results = Items.objects.all()

    menu2 = [
             {'title': "CART", 'url_name': 'cart'},
             ]
    context = {
        'results': results,
        'menu': menu,
        'title': 'A-V-L',
    }
    context['menu2'] = menu2

    return render(request, 'root/search_results.html', context)
