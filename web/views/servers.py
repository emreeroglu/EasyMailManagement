from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server.models import Server
from server.forms import AddServerForm


@login_required(login_url='login')
def servers(request):
    if request.GET:
        add_server = request.GET.get('add_server', '')
        if add_server == "true":
            form = AddServerForm()
            return render(request, 'web/servers.html', {'form': form})
    if request.POST:
        form = AddServerForm(request.POST)
        if form.is_valid():
            new_server = form.save(commit=False)
            new_server.save()
            server_list = Server.objects.all()
            return render(request, "web/servers.html", {'servers': server_list})
        # form is not valid:
        return render(request, 'web/servers.html', {'form': form})
    server_list = Server.objects.all()
    return render(request, "web/servers.html", {'servers': server_list})
