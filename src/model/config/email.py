from model.config.config import Config


class EmailConfig(Config):

    def __init__(self, email) -> None:
        super().__init__()
        self.email = email
