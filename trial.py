import yaml
import os

config_file = os.path.join(os.path.dirname(_file_), 'C:/Users/shamo/Desktop/projects/fullstack-repo/config.yaml')

with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

server_ip = config.get('ip_address')

print(f"Connecting to server at IP address: {server_ip}")