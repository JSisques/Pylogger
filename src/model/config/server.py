from model.config.config import Config


class ServerConfig(Config):
    
    def __init__(self, ip, port, route) -> None:
        super().__init__()
        self.ip = ip
        self.port = port
        self.route = route
