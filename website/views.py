from django.shortcuts import render, redirect
from django.forms import ModelForm

from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content"]


def index(request):
    context = {
        "message": "coucou"
    }
    return render(request, 'website/home.html', context)


def all_messages(request):
    messages = Message.objects.all()
    return render(request, 'website/all.html', context={
        "messages": messages
    })


def show_message(request, message_id):
    message = Message.objects.get(id=message_id)

    return render(request, 'website/show.html', context={
        "message": message
    })


def create(request):
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)  # ne flush pas
            message.save()  # we can do also : form.save
            return redirect("all_messages")
    return render(request, 'website/create.html', {'form': form})


def update(request, message_id):

    message = Message.objects.get(id=message_id)
    form = MessageForm(instance=message)

    if request.method == 'POST':
        form = MessageForm(data=request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('all_messages')

    return render(request, 'website/edit.html', {
        'form': form,
        'message': message
    })


def delete(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('all_messages')
