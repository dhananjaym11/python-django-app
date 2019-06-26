from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Success')
            print('Name:' + form.cleaned_data['name'])
            print('Email:' +  form.cleaned_data['email'])
            print('text:' + form.cleaned_data['text'] )



    form_dict = {'form': form}
    return render(request, 'basicapp/forms_page.html', context=form_dict)