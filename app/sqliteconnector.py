import sqlite3
from sqlite3 import Error
from loguru import logger
from contact import Contact

class SqliteConnector:
    def __init__(self):
        self.db_file = "db/chats.db"
        self.conn = None
        
    def open_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            logger.error(str(e))

    def close_connection(self):
        try:
            self.conn.close()
        except Error as e:
            logger.error(str(e))
            

    def create_tables(self):
        logger.info('#')
        self.open_connection()
        create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                    id TEXT PRIMARY KEY NOT NULL,
                                    server TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    isUser BOOLEAN NOT NULL,
                                    isGroup BOOLEAN NOT NULL,
                                    isMyContact BOOLEAN NOT NULL,
                                    isWAContact BOOLEAN NOT NULL,
                                    isBusiness BOOLEAN NOT NULL,
                                    download_media BOOLEAN DEFAULT FALSE NOT NULL
                                ); """

        try:
            c = self.conn.cursor()
            c.execute(create_contacts_table) 
            c.close()
            self.conn.close()          
        except Error as e:
            logger.error(str(e))


    def add_new_contact(self, contact):
        self.open_connection()
        self.conn.execute('''
                INSERT OR IGNORE INTO contacts (id, server, name, isUser, isGroup, isMyContact, isWAContact, isBusiness, download_media)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (contact.id, contact.server, contact.name, contact.isUser, contact.isGroup, contact.isMyContact, contact.isWAContact, contact.isBusiness, contact.download_media))
        self.conn.commit()
        self.close_connection()
 
    def get_contact_by_id(self, contact_id):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        row = cursor.fetchone()
        if row:
            return Contact(*row)
        return None
    

    def get_groups(self, api_call=False):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, server, name, isUser, isGroup, isMyContact, isWAContact, isBusiness, download_media FROM contacts WHERE server = "g.us"')
        if api_call == True:
            rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
            cursor.close()
            return (rows[0] if rows else None) if False else rows
        else:
            rows = cursor.fetchall()
        return rows
    
    def get_users(self, api_call=False):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, server, name, isUser, isGroup, isMyContact, isWAContact, isBusiness, download_media FROM contacts WHERE server = "c.us"')
        if api_call == True:
            rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
            cursor.close()
            return (rows[0] if rows else None) if False else rows
        else:
            rows = cursor.fetchall()
        return rows