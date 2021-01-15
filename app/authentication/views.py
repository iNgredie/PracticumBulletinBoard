from django.contrib.auth import get_user_model
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string

from .forms import RegistrationForm
from .utils import account_activation_token
from django.urls import reverse



User = get_user_model()


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        email = self.request.POST["email"]
        password = self.request.POST["password1"]

        context = {
            'fieldValues': self.request.POST
        }

        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                messages.error(self.request, 'Password too short')
                return render(self.request, 'authentication/register.html', context)

            user = User.objects.create_user(email=email, password=password)
            user.set_password(password)
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('activate', kwargs={
                           'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://'+current_site.domain+link

            email = EmailMessage(
                email_subject,
                'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
                'noreply@semycolon.com',
                [email],
            )
            email.send(fail_silently=False)
            messages.success(self.request, 'Account successfully created')
            return render(self.request, 'authentication/register.html')

        return render(self.request, 'authentication/register.html')