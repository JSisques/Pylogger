import requests

class Server:

    def __init__(self, ip, port, route="/") -> None:
        self.ip = ip
        self.port = port
        self.route = route
        self.path = "https://" + ip + ":" + port + route
    
    def send_data(self, data) -> str:
        requests.post(self.path, data)
        return data