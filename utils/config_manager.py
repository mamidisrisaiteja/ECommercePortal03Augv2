"""Configuration Manager for reading config.yaml"""
import yaml
import os


class ConfigManager:
    """Manages configuration settings from config.yaml"""
    
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from yaml file"""
        try:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML configuration: {e}")
    
    def get_login_page_url(self):
        """Get login page base URL"""
        return self.config.get('login_page_base_url', 'https://www.saucedemo.com/')
    
    def get_config_value(self, key, default=None):
        """Get any configuration value by key"""
        return self.config.get(key, default)


# Global config instance
config = ConfigManager()
