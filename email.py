class Email:

    def __init__(self, email) -> None:
        self.email = email

    def send_email(self, body) -> str:
        return "Email sended to " + self.email + " with body " + body