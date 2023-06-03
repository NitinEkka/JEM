from django.shortcuts import render
from django.views.generic import CreateView
from .forms import MailForm
from .models import Mail
from django.core.mail import send_mail
# password='zfdexqjthoczmgpq'


def homePage(request):
    form = MailForm()
    if request.method == 'POST':
        form = MailForm(request.POST)
        name = request.POST['name']
        # print(name)
    return render(request, 'index.html', {'form': form})

def mailView(request):
    form = MailForm()
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            send_mail(
                "Test Subject",
                f"Test Message to {name}",
                'nitin.ekka30@gmail.com',
                ['nitin.ekka30@gmail.com'],
                fail_silently=False
            )
    # print(name)

    return render(request, 'mail.html', {'form': form})


