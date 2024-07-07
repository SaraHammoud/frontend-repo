import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

run_localhost = config['run_localhost']

class Client:
    def __init__(self):
        self.run_localhost = run_localhost

    def connect(self):
        if self.run_localhost:
            print("Error: Running on localhost is not allowed.")
        else:
            print("Connecting to server...")

if __name__ == "__main__":
    client = Client()
    client.connect()

