from .forms import ClientForm
from django.core.files import File
from django.shortcuts import redirect
from .models import Client
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'contacts/client_detail.html', {'client': client})


def client_list(request):
    posts = Client.objects.all()
    return render(request, 'contacts/client_list.html', {'posts': posts})



# Create your views here.

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST or None, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.createur = request.user
            client.created_date = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'contacts/client_edit.html', {'form': form}) 







def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form =ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.createur = request.user
            client.created_date = timezone.now()
            client.save()
        return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'contacts/client_edit.html', {'form': form})
