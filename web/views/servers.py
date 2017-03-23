from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server.models import Server


@login_required(login_url='login')
def servers(request):
    server_list = Server.objects.all()
    return render(request, "web/servers.html", {'servers': server_list})
