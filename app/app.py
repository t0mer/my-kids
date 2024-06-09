import requests
from utils import Utils
from loguru import logger
from server import Server
from contact import Contact
from sqliteconnector import SqliteConnector
from confighandler import ConfigHandler

db = SqliteConnector()
utils = Utils()
config_handler = ConfigHandler()
db.create_tables()






contacts_url = 'http://192.168.0.252:3033/client/getContacts/t0mer'
    
if __name__=="__main__":
    # groups = db.get_users(True)
    # print(groups)
    # utils.fetch_and_insert_contacts(contacts_url)
    # config = config_handler.load()
    # print(config)
    # config.chats_update_interval=77
    # config_handler.save(config)
    server = Server()
    server.start()
    