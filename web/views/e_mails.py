from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from electronicmail.forms import AddElectronicMailForm
from server.models import Server


@login_required(login_url='login')
def e_mails(request):
    if request.GET:
        add_server = request.GET.get('add_electronic_mail', '')
        if add_server == "true":
            form = AddElectronicMailForm()
            return render(request, 'web/e_mails.html', {'form': form})
    if request.POST:
        form = AddElectronicMailForm(request.POST)
        if form.is_valid():
            new_email_box = form.save(commit=False)
            new_email_box.user = request.user
            new_email_box.save()
            new_email_box.setup()
            e_mail_list = request.user.electronicmail_set.all()
            return render(request, "web/e_mails.html", {'e_mail_list': e_mail_list})
        # form is not valid:
        return render(request, 'web/e_mails.html', {'form': form})
    e_mail_list = request.user.electronicmail_set.all()
    return render(request, "web/e_mails.html", {'e_mail_list': e_mail_list})
