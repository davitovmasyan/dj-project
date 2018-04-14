from django.test import TestCase
from django.core import mail

from .utils import send_email


class EmailTestCase(TestCase):
    def test_send_email(self):
        send_email(
            subject="Test subject",
            template_name="core/email/blank.html",
            context={
                "recipient_name": "Davit",
            },
            to="davittomasso@gmail.com",
        )

        self.assertEqual(len(mail.outbox), 1)

        email = mail.outbox[0]

        self.assertEqual(email.subject, "Test subject")
        self.assertEqual(email.to, ["davittomasso@gmail.com"])
        self.assertEqual(
            email.body,
            "<h1>Greetings Davit!</h1>",
        )
