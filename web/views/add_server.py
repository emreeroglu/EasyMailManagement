from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server.forms import AddServerForm
from .servers import servers


@login_required(login_url='login')
def add_server(request):

    if request.method == 'POST':
        form = AddServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)
            server.save()
            return servers(request)
        # form is not valid:
        return render(request, 'web/add_server.html', {'form': form})
    form = AddServerForm()
    return render(request, 'web/add_server.html', {'form': form})
