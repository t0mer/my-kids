import yaml
from typing import Any
import shutil
import os
import time
from os import path
from loguru import logger

class Config:
    def __init__(self, wapi_base_url: str, wapi_contacts_url: str, wapi_qr_image_url: str, 
                 wapi_session_status_url: str, wapi_api_token: str, ai_teach_url: str, 
                 ai_detect_url: str, contacts_update_interval: int, chats_update_interval: int, 
                 images_download_interval: int, kids_detection_interval: int):
        self.wapi_base_url = wapi_base_url
        self.wapi_contacts_url = wapi_contacts_url
        self.wapi_qr_image_url = wapi_qr_image_url
        self.wapi_session_status_url = wapi_session_status_url
        self.wapi_api_token = wapi_api_token
        self.ai_teach_url = ai_teach_url
        self.ai_detect_url = ai_detect_url
        self.contacts_update_interval = contacts_update_interval
        self.chats_update_interval = chats_update_interval
        self.images_download_interval = images_download_interval
        self.kids_detection_interval = kids_detection_interval


class ConfigHandler:
    def __init__(self):
        self.config_file = "config/config.yaml"
        self.copy_config_file()



    def copy_config_file(self):
        try:
            if not path.exists(self.config_file):
                shutil.copy('config.yaml', self.config_file)
        except Exception as e:
            logger.error(f"Error copy config file \n {str(e)}")


    def load(self) -> Config:
        with open(self.config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        
        return Config(**config_data)

    def save(self, config: Config):
        config_data = {
            'wapi_base_url': config.wapi_base_url,
            'wapi_contacts_url': config.wapi_contacts_url,
            'wapi_qr_image_url': config.wapi_qr_image_url,
            'wapi_session_status_url': config.wapi_session_status_url,
            'wapi_api_token': config.wapi_api_token,
            'ai_teach_url': config.ai_teach_url,
            'ai_detect_url': config.ai_detect_url,
            'contacts_update_interval': config.contacts_update_interval,
            'chats_update_interval': config.chats_update_interval,
            'images_download_interval': config.images_download_interval,
            'kids_detection_interval': config.kids_detection_interval
        }
        
        with open(self.config_file, 'w') as file:
            yaml.safe_dump(config_data, file)


# Example usage:
# config_handler = ConfigHandler('config.yaml')
# config = config_handler.load()
# config_handler.save(config)
