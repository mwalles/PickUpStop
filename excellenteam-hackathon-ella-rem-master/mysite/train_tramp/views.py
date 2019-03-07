from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, FormView, ListView

from .maps import generate_map
from .models import Person , Consumers
from twilio.rest import Client
from .paths import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


def person_detail(request, pk):
    o = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
            return redirect('add_consume', pk=pk)
    return render(request,"train_tramp/details.html", {'object': o,})

# i = 6
# def getpk():
#     global i
#     i = i+1
#     yield i

# pl = getpk()


def screen_app(request, pk):
    # pk = next(pl)
    m = generate_map(pk)
    stop_name, stop_location = list(path_1.items())[pk]
    stop_name_2, stop_location = list(path_1.items())[pk+1]
    stop_name_3, stop_location = list(path_1.items())[pk+2]

    all_person = Person.objects.all()
    place = []
    for item in all_person:
        place.append(item.places_to_travel)

    html = m.get_root().render()
    html = html.replace("<!DOCTYPE html>\n<head>", "")
    return render(request, "train_tramp/main_screen.html", {
        'map': html, 'object': stop_name, 'pk': pk, 'object_2': stop_name_2, 'object_3': stop_name_3,
        'place_1': place[pk], 'place_2': place[pk+1], 'place_3': place[pk+2]
    })


def person_welcome(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.save()
            return redirect(add_person)
            assert False, form.cleaned_data
    else:
        form = PersonForm()

    return render(request, "train_tramp/person_form.html", {
        'form': form,
    })


class PersonListView(ListView):
    model = Person


def add_person(request):
    return render(request, "train_tramp/added.html", {
    })


class PersonCreateView(CreateView):
    model = Person
    fields = "__all__"


###########################################################################

class ConsumeForm(forms.ModelForm):
    class Meta:
        model = Consumers
        fields = "__all__"


def get_message(send, name, phone):
    # form = PersonForm(request.POST, request.FILES)
    send_SMS(send,f"Hi, {name} is joining you on the ride!!!!!! to connect please call {phone}")


def send_SMS(to, massage):
   account_sid = 'ACdb54a9fd2490c54788e3d66dd30f226f'
   auth_token = '35a8a48b2501585c4415c2b07bd2e38a'
   client = Client(account_sid, auth_token)
   message = client.messages.create(
                        body=massage,
                        from_='+97********12',
                        to=to
                    )


def add_consume(request, pk):
    if request.method == "POST":
        form = ConsumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.save()
            get_message('+972543216766', form['name'].value(), form['phone'].value())
            return redirect(add_person)
            assert False, form.cleaned_data
    else:
        form = ConsumeForm()

    return render(request, f"train_tramp/consumer_form.html", {
        'form': form,
    })


def run(request):
    return redirect(screen_app, pk=6)


class PersonListView(ListView):
    model = Consumers


class PersonCreateView(CreateView):
    model = Consumers
    fields = "__all__"




