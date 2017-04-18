from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from emailbox.forms import AddEMailBoxForm


@login_required(login_url='login')
def personal(request):
    if request.GET:
        add_server = request.GET.get('add_mail_box', '')
        if add_server == "true":
            form = AddEMailBoxForm()
            return render(request, 'web/personal.html', {'form': form})
    if request.POST:
        form = AddEMailBoxForm(request.POST)
        if form.is_valid():
            new_emailbox = form.save(commit=False)
            new_emailbox.user = request.user
            new_emailbox.save()
            emailbox_list = request.user.emailbox_set.all()
            return render(request, "web/personal.html", {'emailboxes': emailbox_list})
        # form is not valid:
        return render(request, 'web/personal.html', {'form': form})
    emailbox_list = request.user.emailbox_set.all()
    return render(request, "web/personal.html", {'emailboxes': emailbox_list})
