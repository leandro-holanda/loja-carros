from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_verification_email(user, request):

    uid = urlsafe_base64_encode(force_bytes(user.pk))

    token = default_token_generator.make_token(user)

    verification_path = reverse(
        'verify_email',
        kwargs={
            'uidb64': uid,
            'token': token
        }
    )

    verification_url = request.build_absolute_uri(verification_path)

    subject = 'Confirme seu cadastro'

    message = f"""
                Olá, {user.first_name or user.username}!

                Obrigado por se cadastrar no nosso marketplace.

                Para ativar sua conta, acesse o link abaixo:

                {verification_url}

                Se você não realizou esse cadastro, ignore este e-mail.
                """

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )