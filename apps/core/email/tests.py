from .utils import send_email


def test_send_email(mailoutbox):
    send_email(
        subject="Test subject",
        template_name="core/email/blank.html",
        context={
            "recipient_name": "Davit",
        },
        to="davitovmasyan@gmail.com",
    )

    assert len(mailoutbox) == 1

    email = mailoutbox[0]

    assert email.subject == "Test subject"
    assert email.to == ["davitovmasyan@gmail.com"]
    assert email.body == "<h1>Greetings Davit!</h1>"
