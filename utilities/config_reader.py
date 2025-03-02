import configparser
import os

class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "configurations", "config.ini")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        self.config.read(config_path)

    def get_url(self):
        return self.config.get('centime', 'url' )

    def get_username(self):
        return self.config.get('centime', 'username')

    def get_password(self):
        return self.config.get('centime', 'password')



