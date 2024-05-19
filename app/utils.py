import requests
from loguru import logger
from contact import Contact
from sqliteconnector import SqliteConnector


class Utils:
    def __init__(self):
        self.db = SqliteConnector()
    
    
    
    def fetch_and_insert_contacts(self,api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                contacts = data.get('contacts', [])
                for contact_json in contacts:
                    try:
                        try:
                            name=contact_json['name']
                        except:
                            name=contact_json['id']['_serialized']
                        contact = Contact(
                            id=contact_json['id']['_serialized'],
                            server=contact_json['id']['server'],
                            name=name,
                            isUser=contact_json['isUser'],
                            isGroup=contact_json['isGroup'],
                            isMyContact=contact_json['isMyContact'],
                            isWAContact=contact_json['isWAContact'],
                            isBusiness=contact_json['isBusiness']
                        )
                        self.db.add_new_contact(contact=contact)
                    except Exception as e:
                        logger.error(f"Error adding contact: {contact_json['id']['_serialized']}. \n {str(e)}")
        else:
            print(f"Failed to fetch data: {response.status_code}")
            
            
            

        