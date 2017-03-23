from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server.forms import AddServerFrom


@login_required(login_url='login')
def add_server(request):
    form = AddServerFrom()
    return render(request, "web/servers.html", {'form': form})
