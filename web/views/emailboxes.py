from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from emailbox.forms import AddEMailBoxForm
from server.models import Server


@login_required(login_url='login')
def emailboxes(request):
    if request.GET:
        add_server = request.GET.get('add_mail_box', '')
        if add_server == "true":
            form = AddEMailBoxForm()
            return render(request, 'web/emailboxes.html', {'form': form})
    if request.POST:
        form = AddEMailBoxForm(request.POST)
        if form.is_valid():
            new_email_box = form.save(commit=False)
            new_email_box.user = request.user
            new_email_box.save()
            new_email_box.setup()
            email_box_list = request.user.emailbox_set.all()
            return render(request, "web/emailboxes.html", {'email_boxes': email_box_list})
        # form is not valid:
        return render(request, 'web/emailboxes.html', {'form': form})
    email_box_list = request.user.emailbox_set.all()
    return render(request, "web/emailboxes.html", {'email_boxes': email_box_list})
