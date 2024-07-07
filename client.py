import configparser

config = configparser.ConfigParser()
config.read('config.ini')

server_ip = config['DEFAULT']['ServerIPAddress']

class Client:
    def __init__(self):
        self.server_ip = server_ip

    def connect(self):
        print(f"Connecting to server at {self.server_ip}")

if __name__ == "__main__":
    client = Client()
    client.connect()
