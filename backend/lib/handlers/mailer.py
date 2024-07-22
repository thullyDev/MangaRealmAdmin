def send_email(subject, body, to_email):
    yag = yagmail.SMTP(SITE_EMAIL, SITE_EMAIL_PASS)

    yag.send(
        to=to_email,
        subject=subject,
        contents=body
    )

    yag.close()

